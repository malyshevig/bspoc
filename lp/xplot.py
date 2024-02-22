
import matplotlib.pyplot as plt

from pandas import Series
from hampel import hampel
from hampel.result import Result


def deviation_array( data: Series) -> ([], []):
    result: Result = hampel(data, window_size=50, n_sigma=30.0)

    dev_data = [data[idx] for idx in result.outlier_indices]
    return result.outlier_indices, dev_data, result.filtered_data

def deviation_array2( data: Series) -> ([], []):
    idxs = []
    outl = []
    filtered = []

    mean = data.mean()
    std = data.std()

    for idx in range(len(data)):
        if abs(data[idx] - mean) >= std*6:
            idxs .append(idx)
            outl . append(data[idx])
        else:
            filtered.append(data[idx])

    return idxs, outl, filtered


class LatencyPlotter:
    DEVIATION_QUANTILE = 0.9

    def __init__(self, t_arr: Series, p99: Series, lmax: Series,
                 title: str, max_of_max, avg_of_max, avg_of_p99):
        self.t_arr:Series = t_arr
        self.p99:Series=p99
        self.lmax:Series=lmax

        self.title = title
        _, self.deviation_data, self.lmax_filtered = deviation_array2(self.lmax)

        self.max_of_max = max_of_max
        self.avg_of_max = avg_of_max
        self.avg_of_p99 = avg_of_p99

    def has_deviation(self)-> bool:
        return len(self.deviation_data)>0

    def wider(self, a, b):
        _mean = (a + b) // 2
        delta = (_mean - a) // 4 + 1
        a -= delta
        b += delta

        a = max(0,a)
        return a,b

    def plot(self):
        # assume

        fig, top, middle, bottom = None, None, None, None
        if self.has_deviation():
            fig, (top, middle, bottom) = plt.subplots(3, 1, sharex=True)
        else:
            fig, (middle, bottom) = plt.subplots(2, 1, sharex=True)

        fig.set_size_inches(18, h=12, forward=True)
        fig.subplots_adjust(hspace=0.1)  # adjust space between axes

        if top:
            top.set_title(self.title)
        else:
            middle.set_title(self.title)

        if top:
            top.plot(self.lmax )
            top.plot(self.p99, color="orange")   # in order to print legend
            middle.plot(self.lmax)
        else:
            middle.plot(self.lmax)
            middle.plot(self.p99, color="orange")  # in order to print legend

        bottom.plot(self.p99, color="orange")

        if top:
            dev_min = min(self.deviation_data)
            dev_max = max(self.deviation_data)
            dev_min, dev_max = self.wider(dev_min, dev_max)

            top.set_ylim(dev_min, dev_max)  # outliers only

        norm_min = min(self.lmax_filtered)
        norm_max = max(self.lmax_filtered)
        norm_min, norm_max = self.wider(norm_min, norm_max)

        norm_min = max(20,norm_min)
        middle.set_ylim(norm_min, norm_max)  # most of the data

        p99_min = 0
        p99_max = round(max(self.p99))
        _, p99_max = self.wider(p99_min, p99_max)

        p99_max = max(p99_max,3)
        bottom.set_ylim(p99_min, p99_max)

        if top:
            top.spines.bottom.set_visible(False)

        middle.spines.bottom.set_visible(False)
        middle.spines.top.set_visible(False)
        middle.xaxis.set_ticks_position("none")

        if top:
            top.xaxis.tick_top()
            top.tick_params(labeltop=False)  # don't put tick labels at the top

        bottom.spines.top.set_visible(False)
        bottom.xaxis.tick_bottom()

        if top:
            top.grid(True)

        middle.grid(True)
        bottom.grid(True)

        if top:
            top.legend(["max, ms", "p99, ms"])
        else:
            middle.legend(["max, ms", "p99, ms"])

        xticks = self.t_arr

        xt_num = 15
        rt = len(xticks)
        pos = [x for x in range(0, rt, rt // xt_num - 1)]
        pos_levels = [xticks[x] for x in pos]
        bottom.set_xticks(pos, pos_levels)

        if top:
            top.hlines(self.max_of_max, xmin=0, xmax=1400, colors="red", linestyles='dashed')
            top.text(-50, self.max_of_max, f"max={self.max_of_max:.2f}", ha='left', va='baseline', fontsize="large")
        else:
            middle.hlines(self.max_of_max, xmin=0, xmax=1400, colors="red", linestyles='dashed')
            middle.text(-50, self.max_of_max, f"max={self.max_of_max:.2f}", ha='left', va='baseline', fontsize="large")

        middle.hlines(self.avg_of_max, xmin=0, xmax=1400, colors="red", linestyles='dashed')
        middle.text(-50, self.avg_of_max, f"avg={self.avg_of_max:.2f}", ha='left', va='baseline', fontsize="large")

        bottom.hlines(self.avg_of_p99, xmin=0, xmax=1400, colors="red", linestyles='dashed')
        bottom.text(-50, self.avg_of_p99, f"p99={self.avg_of_p99:.2f}", ha='left', va='baseline', fontsize="large")

        bottom.set_xlabel("Time")
        middle.set_ylabel("Milliseconds")

        return fig


def plot_layers(arr,arr2, xticks):
    fig,(top, middle, bottom) = plt.subplots(3, 1, sharex=True)
    fig.set_size_inches(18, h=9, forward=True)

    fig.subplots_adjust(hspace=0.1)  # adjust space between axes
    # zoom-in / limit the view to different portions of the data
    top.set_title("This is just a prototype")

    idx, data,_ = deviation_array(arr)
    for i in range(len(idx)):
        print (f"{idx[i]}: {data[i]}")


    top.plot(arr)
    top.plot(arr2)
    middle.plot(arr)
    bottom.plot(arr2, color="orange")

    top.set_ylim(3000, 4500)  # outliers only
    middle.set_ylim(3, 150)  # most of the data
    bottom.set_ylim(0, 3)

    # hide the spines between ax and middle
    top.spines.bottom.set_visible(False)

    middle.spines.bottom.set_visible(False)
    middle.spines.top.set_visible(False)
    middle.xaxis.set_ticks_position("none")

    top.xaxis.tick_top()
    top.tick_params(labeltop=False)  # don't put tick labels at the top
    bottom.spines.top.set_visible(False)
    bottom.xaxis.tick_bottom()

    top.grid(True)
    middle.grid(True)
    bottom.grid(True)

    top.legend(["max, ms","p99, ms"])

    xt_num = 15
    rt = len(xticks)
    pos = [x for x in range(0, rt, rt//xt_num-1)]
    pos_lavels = [xticks[x] for x in pos]
    bottom.set_xticks(pos, pos_lavels)

    top.hlines(4230, xmin=0, xmax=1400, colors="red", linestyles='dashed')
    top.text(-50, 4230, "max=4230", ha='left', va='baseline', fontsize="large")

    bottom.set_xlabel("Time")
    middle.set_ylabel("Milliseconds")


    fig.set_size_inches(18, h=9, forward=True)

    return fig

