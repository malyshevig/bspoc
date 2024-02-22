import logging
import pathlib
import sys

import pandas
from datetime import timedelta
from pandasql import sqldf

from .conf import Config
from .util import *
from .draw import *
from .conf import *


logging.basicConfig(stream=sys.stdout,encoding='utf-8', format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)




class FileNames:

    def __init__(self, config: Config):
        self.config = config
        fname = config.filename[:-4]
        self.base_filename = str(pathlib.Path(config.directory).joinpath(fname))

        self.cut_warmup_base_filename = self.base_filename + "_cut_warmup"

    def __files__(self, base_filename) -> dict:
        r = {}
        r["data"] = base_filename + "_data.xlsx"
        r["result_all"] = base_filename + "_result_all"
        r["Find balance"] = base_filename + "_find_balance"
        r["Get balance"] = base_filename + "_get_balance"
        r["Reserve balance"] = base_filename + "_reserve_balance"
        r["Find balance_mixed"] = base_filename + "_find_balance_mixed"
        r["Get balance_mixed"] = base_filename + "_get_balance_mixed"
        r["Reserve balance_mixed"] = base_filename + "_reserve_balance_mixed"
        r["result_all_mixed"] = base_filename + "_result_all_mixed"
        r["metrics"] = base_filename + "_metrics"
        r["rps"] = base_filename + "_rps"

        return r

    def files(self) -> map:
        return self.__files__(self.base_filename)

    def cw_files(self) -> map:
        return self.__files__(self.cut_warmup_base_filename)


class ReportResult:
    def __init__(self):
        self.vf_result = None
        self.max_of_max = None
        self.avg_of_max = None
        self.avg_of_p99 = None
        self.avg_of_stddev = None
        self.avg_of_rps = None

    def __str__(self):
        s = f"max(max)={self.max_of_max}\n" + \
            f"avg(max)={self.avg_of_max}\n" + \
            f"avg(p99)={self.avg_of_p99}\n" + \
            f"avg(rps)={self.avg_of_rps}\n" + \
            f"avg(stddev)={self.avg_of_stddev}"

        return s

    def __repr__(self):
        return str(self)


class Report:
    steps_list = ["'Find balance'", "'Get balance'", "'Reserve balance'"]
    label = ["p99, ms", "max, ms", ]
    legend = ["p99", "max"]
    cols = ["latency99", "latency_max", ]

    def __init__(self, config: Config, df: DataFrame, steps=None):
        self.config = config
        self.steps = steps
        self.src_df = df
        self.data = self.filter(vf=df, steps=self.steps, sess=config.session)
        self.data = self.__prepare_df__(self.data)
        self.data_warmup_cut = self.__cut_warmup__(self.data)

    def __prepare_df__(self, vf):
        period_sec = self.config.period

        # sort by date time
        vf.sort_values(by=['Time'], inplace=True)
        # remove redundant columns
        vf = vf.filter(items=["Time", "step", "session_id", "current_operation", "ok.request.rps",
                              "ok.latency.max", "ok.latency.mean", "ok.latency.min",
                              "ok.latency.percent99", "ok.latency.stddev"])
        # calculate base second num
        base_time_str = vf["Time"][0]
        base_time_secs = sec(base_time_str)
        base_time = datetime.strptime(base_time_str, "%Y-%m-%d %H:%M:%S")

        def calc_period(tm: str) -> int:
            return int((sec(tm) - base_time_secs) // period_sec)

        # add columns for period and period_start calculation further
        vf["period"] = vf.Time
        vf["period_start"] = vf.Time
        #
        columns = vf.columns
        # convert to numpy, calculate period , convert back to DataFrame
        arr = vf.to_numpy()
        for r in arr:
            period = calc_period(r[0])
            r[-2] = period
            period_start = base_time + timedelta(seconds=period * period_sec)
            #        r[-1] = period_start.strftime("%Y-%m-%d %H:%M:%S")
            r[-1] = period_start.strftime("%H:%M:%S")
        # convert back to DataFrame
        vf = DataFrame(arr, columns=columns)

        if self.config.remove_head > 0:
            left = self.config.remove_head * 60 // period_sec
            vf = vf[vf["period"] > left]

        return vf

    def __cut_warmup__(self, vf: DataFrame):
        period_sec = self.config.period
        warming_period = self.config.warmup * 60 // period_sec
        stopping_period = self.config.warmup * 60 // period_sec
        max_period = vf["period"].max()
        left = warming_period
        right = max_period - stopping_period
        vf = vf[vf["period"] > left]
        vf = vf[vf["period"] < right]

        return vf

    def filter(self, vf, steps, sess=None):
        assert vf is not None

        current_operation = "bombing"
        # make str of steps to filter
        steps_str = ",".join(steps)
        # filter steps and current_operation
        reqs = f"select * from vf where step in ({steps_str}) and current_operation='{current_operation}'"
        if sess:
            reqs = reqs + " " + f"and session_id='{sess}'"
        vf = sqldf(reqs)
        return vf

    @staticmethod
    def aggregate(vf) -> DataFrame:
        assert vf is not None

        vf1 = sqldf("select session_id,period,period_start, step,  "
                    "avg(vf.'ok.latency.percent99') latency99, " +
                    "max(vf.'ok.latency.max') latency_max, " +
                    "min(vf.'ok.latency.min') latency_min, " +
                    "avg(vf.'ok.latency.stddev') latency_stddev, " +
                    "avg(vf.'ok.latency.mean') latency_mean, " +
                    "avg(vf.'ok.request.rps') rps " +
                    "from vf " +
                    "group by  period, period_start, session_id, step;")

        vf = vf1
        vf2: DataFrame = sqldf("select period, period_start, avg(vf.'latency99') latency99, " +
                               "max(vf.'latency_max') latency_max, " +
                               "min(vf.'latency_min') latency_min, " +
                               "avg(vf.'latency_mean') latency_mean, " +
                               "avg(vf.'latency_stddev') latency_stddev, " +
                               "sum(vf.'rps') rps " +
                               "from vf group by period, period_start;")
        vf_result = vf2
        return vf_result

    @staticmethod
    def calc_aggregates(vf):
        max_of_max = vf["latency_max"].max()
        avg_of_max = vf["latency_max"].mean()
        avg_of_p99 = vf["latency99"].mean()
        avg_of_stddev = vf["latency_stddev"].mean()
        avg_of_rps = vf["rps"].mean()

        rr: ReportResult = ReportResult()
        rr.max_of_max = max_of_max
        rr.avg_of_max = avg_of_max
        rr.avg_of_p99 = avg_of_p99
        rr.avg_of_stddev = avg_of_stddev
        rr.avg_of_rps = avg_of_rps
        return rr


def generate(config: Config):
    fnames = FileNames(config)
    fname = config.filename

    if not fname.endswith(".csv"):
        raise ValueError(f"expected csv file, but {fname} is given")
    fname = str(pathlib.Path(config.directory).joinpath(fname))

    df = pandas.read_csv(fname)

    steps_list = ["'Find balance'", "'Get balance'", "'Reserve balance'"]
    # All steps
    report_all_steps(config, df, fnames, steps_list)

    # Generate pics for every step
    for step in steps_list:
        report_step(config, df, fnames, step)


def report_step(config, df, fnames, step):
    key = step[1:-1]
    steps_list = [step]

    rep = Report(config, df, steps_list)
    result_df = rep.aggregate(rep.data)
    cw_result_df = rep.aggregate(rep.data_warmup_cut)
    rr = rep.calc_aggregates(cw_result_df)
    rr.vf_result = result_df

    title = f"{config.technology} / {key}"

    draw = ReportDraw(title, result_df, rr)
    latencyfig = draw.draw_latency()
    latencyfig.savefig(fnames.files()[key] + ".png")

    latencyMixedfig = draw.drawLatencyMixed()
    latencyMixedfig.savefig(fnames.files()[key + "_mixed"] + ".png")

    # Draw reports with warn up cut off
    draw = ReportDraw(title, cw_result_df, rr)
    latencyfig = draw.draw_latency()
    latencyfig.savefig(fnames.cw_files()[key] + ".png")

    latencyMixedfig = draw.drawLatencyMixed()
    latencyMixedfig.savefig(fnames.cw_files()[key + "_mixed"] + ".png")


def save_metrics(metrics_name, rr):
    with open(metrics_name, "wt") as fd:
        fd.writelines([str(rr)])


def report_all_steps(config, df, fnames, steps_list):
    rep = Report(config, df, steps_list)
    result_df = rep.aggregate(rep.data)
    cw_result_df = rep.aggregate(rep.data_warmup_cut)
    rr = rep.calc_aggregates(cw_result_df)
    rr.vf_result = result_df

    # Draw reports
    title = f"{config.technology} / "

    draw = ReportDraw(title, result_df, rr)

    rpsfig = draw.draw_rps()
    rpsfig.savefig(fnames.files()["rps"] + ".png")

    latencyfig = draw.draw_latency()
    latencyfig.savefig(fnames.files()["result_all"] + ".png")

    latencyMixedfig = draw.drawLatencyMixed()
    latencyMixedfig.savefig(fnames.files()["result_all_mixed"] + ".png")

    # Draw reports with warn up cut off
    draw = ReportDraw(title, cw_result_df, rr)
    rpsfig = draw.draw_rps()
    rpsfig.savefig(fnames.cw_files()["rps"] + ".png")

    latencyfig = draw.draw_latency()
    latencyfig.savefig(fnames.cw_files()["result_all"] + ".png")

    latencyMixedfig = draw.drawLatencyMixed()
    latencyMixedfig.savefig(fnames.cw_files()["result_all_mixed"] + ".png")

    metrics_name = fnames.files()["metrics"] + ".txt"
    save_metrics(metrics_name, rr)

