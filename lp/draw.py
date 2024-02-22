from pandas import DataFrame

from . import xplot
from .common import ReportResult


class ReportDraw:
    def __init__(self, title: str, df: DataFrame, aggregates: ReportResult):
        self.df = df
        self.title = title
        self.rr = aggregates

    def draw_rps(self):
        title_rps = f"{self.title} / Throughput"
        colormap = "summer"
        label = "throughput, rps"
        legend = "throughput"

        cols = ["rps"]
        rr = self.rr

        plot = self.df.plot(x="period_start", y=cols, figsize=(18, 10),
                            grid=True, kind="line", title=title_rps,
                            legend=True, subplots=True,
                            xlabel="Time", colormap=colormap)

        #plot[0].legend(legend)
        plot[0].set_ylabel(label)

        y_level = rr.avg_of_rps
        y_text = f"rps={rr.avg_of_rps:.0f}"

        plot[0].axhline(y_level, color="red", ls='--')
        plot[0].text(2, y_level, y_text, ha='left', va='baseline', fontsize="large")

        fig = plot[0].get_figure()
        return fig

    def draw_latency(self):
        rr = self.rr

        label = ["p99, ms", "max, ms", ]
        legend = ["p99", "max"]
        cols = ["latency99", "latency_max", ]

        levels = [
            [(rr.avg_of_p99, f"p99={rr.avg_of_p99:.2f}")],
            [(rr.max_of_max, f"max={rr.max_of_max:.2f}"),
             (rr.avg_of_max, f"avg={rr.avg_of_max:.2f}"),
             ]]

        title_latency = f"{self.title} / Latency"

        plot = self.df.plot(x="period_start", y=cols, figsize=(18, 10),
                            grid=True, kind="line", title=title_latency,
                            legend=True, subplots=True,
                            xlabel="Time", colormap=None)

        for idx, _ in enumerate(plot):
            plot[idx].legend([legend[idx]])
            plot[idx].set_ylabel(label[idx])

            for _, l in enumerate(levels[idx]):
                y_level = l[0]
                y_text = l[1]

                plot[idx].axhline(y_level, color="red", ls='--')
                plot[idx].text(2, y_level, y_text, ha='left', va='baseline', fontsize="large")

        fig = plot[0].get_figure()
        return fig

    def drawLatencyMixed(self):
        rr = self.rr
        title_latency = f"{self.title} / Latency"

        plot = xplot.LatencyPlotter(t_arr=self.df["period_start"], p99=self.df["latency99"],
                                    lmax=self.df["latency_max"],
                                    title=title_latency, max_of_max=rr.max_of_max,
                                    avg_of_max=rr.avg_of_max,
                                    avg_of_p99=rr.avg_of_p99)

        return plot.plot()
