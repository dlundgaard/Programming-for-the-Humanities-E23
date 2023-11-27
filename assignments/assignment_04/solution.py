import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker
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
        plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(1)) # show ticks for each timestep, but only labels for every fifth
    plt.margins(x = 0)

def time_series_visualization(
    time_series, 
    output_path, 
    title = "",
    xlabel = "", 
    ylabel = "",
    caption = ""
):
    assert output_path.endswith(".png"), "Output file must be a .png-file."
    plt.figure()

    plt.imshow(time_series, aspect="auto", cmap = "plasma", vmin = 0, vmax = 20)
    cbar = plt.colorbar()
    cbar.ax.set_yticks([0, 10, 20])
    cbar.set_label(label = "Inflammation Level", rotation = 270, labelpad = 10)

    decorate(title, xlabel, ylabel, caption)

    horizontal_paddding = 0.1
    plt.subplots_adjust(
        left = horizontal_paddding, 
        right = 1
    )
    plt.savefig(output_path, dpi = 300)
    print(f"[Saved time series visualization to {output_path}]")

def time_series_stacking(
    time_series, 
    output_path, 
    n_series = 10,
    title = "", 
    xlabel = "", 
    ylabel="",
    caption = ""
):
    figure, axes = plt.subplot_mosaic(
        ";".join([str(i) + "A" for i in range(n_series)]), 
        figsize = (12, 6), 
        width_ratios=(0.46, 0.54)
    )
    series = time_series.sample(n_series)

    for i, (patient_id, time_series) in enumerate(series.iterrows()):
        plt.sca(axes[str(i)])
        plt.plot(time_series)
        plt.plot(series.T, alpha = 0.1, linewidth = 0.8, color = "black")
        decorate()
        plt.yticks([])
        plt.gca().set_ylabel(series.index[i], rotation = "horizontal")
        if i + 1 < n_series:
            plt.gca().xaxis.set_ticklabels([])
    
    decorate(xlabel = "Timestep") # last axes

    plt.sca(axes["0"]) # add title to first axes
    decorate(title = "Separate Time Series")

    plt.sca(axes["A"])
    plt.imshow(series, aspect="auto", cmap = "plasma", vmin = 0, vmax = 20)
    plt.yticks(range(len(series)), series.index)
    decorate(title = "Stacked time series", xlabel = xlabel, ylabel = ylabel, caption = caption)

    cbar = plt.colorbar()
    cbar.ax.set_yticks([0, 10, 20])
    cbar.set_label(label = "Inflammation Level", rotation = 270, labelpad = 10)

    horizontal_paddding = 0.07
    plt.subplots_adjust(
        left = horizontal_paddding, 
        right = 1
    )
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
    g.fig.suptitle("Within-Region Correlations of Happiness Predictors", y = 1.05, fontweight = 600, fontsize = 16)
    g.fig.set_size_inches(9, 8)
    g.savefig(output_path, dpi = 200)
    print(f"[Saved pairplot to {output_path}]")

if __name__ == "__main__":
    mock_dataset = "01"
    dataset = pd.read_csv(f"dat/series/series-{mock_dataset}.csv", header = None)

    # time_series_visualization(
    #     dataset, 
    #     output_path = f"output/series_{mock_dataset}.png", 
    #     title = "Patient Inflammation Development", 
    #     xlabel = "Timestep", 
    #     ylabel = "Patient ID",
    #     caption = "Dataset: " + mock_dataset
    # )

    time_series_stacking(
        dataset, 
        output_path = f"output/series_{mock_dataset}_stacking.png", 
        title = "Overlaid/Stacked Time Series", 
        xlabel = "Timestep", 
        ylabel = "Patient ID",
        caption = "Dataset: " + mock_dataset
    )

    # regions_pairplot(
    #     regions = ["Western Europe", "South Asia"], 
    #     output_path = "output/regions_pairplot.png"
    # )
