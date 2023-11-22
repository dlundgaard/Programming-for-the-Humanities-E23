import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import ticker
plt.style.use("theme.mplstyle")
from cycler import cycler
import seaborn as sns

def decorate(
    title = "",
    xlabel = "Timestep", 
    ylabel = "Value",
    caption = ""
):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title + "\n", fontsize = 14)
    plt.figtext(0.9, 0.05, caption, horizontalalignment="right", fontsize=5)

    plt.margins(x = 0)
    plt.gca().xaxis.set_minor_locator(ticker.MultipleLocator(1)) # show ticks for each timestep, but only labels for every fifth
    plt.grid(True, axis = "both", which="both") # show gridlines forboth axes

def time_series_visualization(
    time_series, 
    output_path, 
    title = "Time Series Developments",
    xlabel = "Timestep", 
    ylabel = "Value",
    caption = ""
):
    assert output_path.endswith(".png"), "Output file must be a .png-file."
    plt.figure()
    plt.gca().set_prop_cycle(cycler(color=plt.rcParams["axes.prop_cycle"]) * cycler(linestyle=["-", "--", "-.", ":"])) # cycle through custom colors

    plt.plot(time_series, marker = "o", markersize = 1, linewidth = 0.8, alpha = 0.8)

    decorate(title, xlabel, ylabel, caption)
    plt.ylim((0, time_series.values.max() * 1.05)) # leave 5% of padding between highest datapoint and axis "roof"
    plt.legend(plt.gca().lines, time_series.index, title = "Series ID", bbox_to_anchor = (1, 0.5), loc = "center left", ncol = 2)

    plt.savefig(output_path, dpi = 300)
    print(f"[Saved time series visualization to {output_path}]")

def time_series_stacking(
    time_series, 
    output_path, 
    n_series = 8,
    caption = ""
):
    figure, axes = plt.subplot_mosaic(";".join(["A" + str(i) for i in range(n_series)]), figsize = (13.5, 4.8))
    series = time_series.sample(n_series, axis = 1)

    plt.sca(axes["A"])
    plt.plot(series, marker = "o", markersize = 1, linewidth = 0.8, alpha = 0.8)
    plt.title("Stacked time series")
    decorate(title = "Overlaid/stacked Time Series", caption = "")

    for i, (series_id, time_series) in zip(range(n_series), series.items()):
        plt.sca(axes[str(i)])
        plt.plot(time_series, marker = "o", markersize = 1, linewidth = 0.8, alpha = 0.8, color = "C" + str(i))
        decorate(ylabel="")
        plt.ylim((0, 20))
        if i + 1 < n_series:
            plt.gca().xaxis.set_ticklabels([])
    
    plt.sca(axes["0"])
    decorate(title = "Separate Axes per Time Series", xlabel="Timestep", ylabel = "", caption = caption)

    plt.legend(axes["A"].lines, series.index, title = "Series ID", bbox_to_anchor = (1, 0), loc = "center left")

    plt.savefig(output_path, dpi = 300)
    print(f"[Saved time series stacking comparison to {output_path}]")

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
    g.fig.suptitle("Within- and Between Region Correlations of Happiness Predictors", y = 1.05, fontweight = 600, fontsize = 16)
    g.fig.set_size_inches(9, 8)
    g.savefig(output_path, dpi = 200)
    print(f"[Saved pairplot to {output_path}]")

if __name__ == "__main__":
    mock_dataset = "01"
    dataset = pd.read_csv(f"dat/series/series-{mock_dataset}.csv", header = None).T # transposing to get each series as column

    time_series_visualization(
        dataset, 
        output_path = "output/series_{mock_dataset}.png", 
        title = "Time Series Development", 
        caption = "Dataset: " + mock_dataset
    )

    time_series_stacking(
        dataset, 
        output_path = f"output/series_{mock_dataset}_stacking.png", 
        caption = "Dataset: " + mock_dataset
    )

    regions_pairplot(
        regions = ["Western Europe", "South Asia"], 
        output_path = "output/regions_pairplot.png"
    )
