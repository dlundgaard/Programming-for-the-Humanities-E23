import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker
from cycler import cycler
plt.style.use("assets/theme.mplstyle")

def decorate(
    title = "",
    xlabel = "", 
    ylabel = "",
    caption = "",
    set_ticks = False
):
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if title:
        plt.title(title + "\n", fontsize = 14)
    if caption:
        plt.figtext(0.9, 0.05, caption, horizontalalignment="right", fontsize=5)
    if set_ticks:
        plt.gca().xaxis.set_minor_locator(ticker.MultipleLocator(1)) # show ticks for each timestep, but only labels for every fifth
    plt.margins(x = 0)

def time_series_visualization(
    time_series, 
    output_path, 
    n_series = None,
    title = "",
    xlabel = "", 
    ylabel = "",
    caption = "",
):
    assert output_path.endswith(".png"), "Output file must be a .png-file."
    plt.figure()
    series = time_series.sample(n_series, axis = "columns") if n_series else time_series

    if n_series and n_series > 10:
        plt.gca().set_prop_cycle(cycler(color=plt.rcParams["axes.prop_cycle"]) * cycler(linestyle=["-", "--", "-.", ":", (0, (1, 10)), (0, (5, 1))])) # cycle through custom colors

    plt.plot(series, marker = "o", markersize = 1, linewidth = 0.8, alpha = 0.8)

    plt.ylim((0, series.values.max() * 1.05)) # leave 5% of padding between highest datapoint and axis "roof"
    plt.legend(plt.gca().lines, series.columns, title = "Series ID", bbox_to_anchor = (1, 0.5), loc = "center left", ncol = 2)
    decorate(title, xlabel, ylabel, caption, set_ticks=True)

    horizontal_paddding = 0.2
    plt.subplots_adjust(
        left = horizontal_paddding, 
        right = 1 - horizontal_paddding
    )
    plt.savefig(output_path, dpi = 300)
    print(f"[Exported time series visualization to {output_path}]")

def time_series_stacking(
    time_series, 
    output_path, 
    n_series = 10,
    title = "", 
    xlabel = "", 
    ylabel="",
    caption = ""
):
    figure, axes = plt.subplot_mosaic(";".join(["A" + str(i) for i in range(n_series)]), figsize = (12, 6))
    series = time_series.sample(n_series, axis = 1)

    plt.sca(axes["A"])
    plt.plot(series, marker = "o", markersize = 1, linewidth = 0.8, alpha = 0.8)
    plt.ylim((0, 20))
    plt.title("Stacked time series")
    decorate(title = "Overlaid/Stacked Time Series", set_ticks=True)

    for i, (series_id, time_series) in zip(range(n_series), series.items()):
        plt.sca(axes[str(i)])
        plt.plot(time_series, marker = "o", markersize = 1, linewidth = 0.8, alpha = 0.8, color = "C" + str(i))
        plt.plot(series, linewidth = 0.4, alpha = 0.2, color = "black")
        decorate(ylabel="", set_ticks=True)
        plt.ylim((0, 20))
        if i + 1 < n_series:
            plt.gca().xaxis.set_ticklabels([])
    decorate(xlabel = "Timestep") # last axes

    plt.sca(axes["0"])
    decorate(title = "Separate Axes per Time Series", xlabel="Timestep", ylabel = "", caption = caption)

    plt.legend(axes["A"].lines, series.index, title = "Series ID", bbox_to_anchor = (1, 0), loc = "center left")

    horizontal_paddding = 0.07
    plt.subplots_adjust(
        left = horizontal_paddding, 
        right = 1 - horizontal_paddding
    )
    plt.savefig(output_path, dpi = 300)
    print(f"[Exported time series stacking comparison to {output_path}]")

def regions_pairplot(regions, output_path):
    df = pd.read_csv("dat/world-happiness-report-2021.csv")[[
        "Regional indicator", 
        "Ladder score", 
        "Logged GDP per capita", 
        "Healthy life expectancy", 
        "Freedom to make life choices", 
        "Generosity", 
        "Perceptions of corruption"
    ]]
    g = sns.pairplot(
        df[df["Regional indicator"].isin(regions)], 
        hue = "Regional indicator", 
        kind = "reg", 
        diag_kind="kde",
    )
    g.fig.suptitle("Within-Region Correlations of Happiness Predictors", y = 1.05, fontweight = 600, fontsize = 16)
    g.fig.set_size_inches(9, 8)
    g.savefig(output_path, dpi = 200)
    print(f"[Exported pairplot to {output_path}]")

if __name__ == "__main__":
    mock_dataset = "01"
    dataset = pd.read_csv(f"dat/series/series-{mock_dataset}.csv", header = None).T

    time_series_visualization(
        dataset, 
        output_path = f"output/series_{mock_dataset}.png", 
        n_series = 20,
        title = "Patient Inflammation Development", 
        xlabel = "Timestep", 
        ylabel = "Patient ID",
        caption = "Dataset: " + mock_dataset
    )

    time_series_stacking(
        dataset, 
        output_path = f"output/series_{mock_dataset}_stacking.png", 
        n_series = 10,
        title = "Overlaid/Stacked Time Series", 
        xlabel = "Timestep", 
        ylabel = "Patient ID",
        caption = "Dataset: " + mock_dataset
    )

    regions_pairplot(
        regions = ["Western Europe", "South Asia"], 
        output_path = "output/regions_pairplot.png"
    )
