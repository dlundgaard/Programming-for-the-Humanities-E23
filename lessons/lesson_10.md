# Lesson 10: Data Visualization #

### Learning outcomes ###

* Data visulization with Python.
* Plot simple and multiple graphs in a single figure.
* Use `seaborn` to make publication-ready graphs

While tabular data formats are good for storing and manipulating heterogenous 2d data, they do not facilitate a deep understanding of data. Data visualization is a powerful tool to better understand the properties of our data, it allows us to expose patterns, correlations, and trends that cannot be obtained when data is in a table or dataframe, or, as the mathematician Richard Hamming once said, 'the purpose of computing is insight, not numbers,' and data visualization is one of the best ways to develop that insight. With Python we can use several data visualization modules (ex. `matplotlib`, `seaborn`, `plotly`, `bokeh`) to create complex visualizations both for data understanding and communication.

## Ten Rules of Visualization ##

1. Know your Audience
2. Identify your Message
3. Adapt the Figure to the Support Medium
4. Captions are not optional
5. Do not Trust the Defaults
6. Use Color Effectively
7. Do not Mislead the Reader
8. Avoid 'chartjunk'
9. Message Trumps Beauty
10. Get the Right Tool


For more examples of the ten rules, See Rougier, N. P., Droettboom, M., & Bourne, P. E. (2014). Ten Simple Rules for Better Figures. PLoS Computational Biology, 10(9), e1003833. https://doi.org/10.1371/journal.pcbi.1003833

### Data-Ink Ratio ###

<img src="https://render.githubusercontent.com/render/math?math=\text{Data-Ink Ratio}=\Large\frac{\text{Data-Ink}}{\text{Total ink used to print the graphic}}">


The Data-Ink ratio is a concept introduced by [_Edward Tufte_](https://www.edwardtufte.com/tufte/), a famous American statistician whose work has contributed significantly to designing effective data presentations. In his 1983 book, 'The Visual Display of Quantitative Data', he stated the goal:

"Above all else show the data"
(Tufte, 1983)

"A large share of ink on a graphic should present data-information, the ink changing as the data change. Data-ink is the non-erasable core of a graphic, the non-redundant ink arranged in response to variation in the numbers represented."
(Tufte, 1983)

Tufte refers to data-ink as the non-erasable ink used for the presentation of data. If data-ink would be removed from the image, the graphic would lose the content. Non-Data-Ink on the other hand is the ink that does not transport information but it is used for scales, labels and edges. The data-ink ratio is the proportion of Ink that is used to present actual data compared to the total amount of ink (or pixels) used in the entire display. (Ratio of Data-Ink to non-Data-Ink).

## Data visualization with Python and `matplotlib` ##

Python does not have an official plotting library, but if there was one, it would be `matplotlib`. `matplotlib` is a comprehensive library for creating static, animated, and interactive visualizations in Python. [Here](https://matplotlib.org/cheatsheets/_images/cheatsheets-1.png) is an excellent cheat sheet for `matplotlib` in case your rote learning resources are getting depleted.

### Read and visualize series data ###

Start by making a `series_visualization.py` file and read one of the tabular files from `data/` as a `numpy` array.

```py
import numpy

data = np.loadtxt(fname='data/series-01.csv', delimiter=',')
```

And run the script in interactive mode, inspect the data and check the dimensions

```sh
$ python -i series_visualization.py
>>> data
array([[0., 0., 1., ..., 3., 0., 0.],
       [0., 1., 2., ..., 1., 0., 1.],
       [0., 1., 1., ..., 2., 1., 1.],
       ...,
       [0., 1., 1., ..., 1., 1., 1.],
       [0., 0., 0., ..., 0., 2., 0.],
       [0., 0., 1., ..., 1., 1., 0.]])
>>> data.shape
(60, 40)
```

We see that the array has 60 objects measured on 40 variables. In this case each object is a person and each variable is a person's daily inflammation rate (over 40 days). In other words, we have a inflammation rate time series and each variable (columns) represent the rate of inflammation at a given day. 

#### Visual inspection of a numpy array ####

Add simple array visualization to `series_visualization.py` and save the files to your `figures` subdirectory.

```py
import matplotlib.pyplot as plt
image = plt.imshow(data)
plt.savefig('figures/my_array.png')
plt.close()
```

And execute. Now you can open your `my_array.png` file and you can inpect the matplotlib object


```sh
$ python -i series_visualization.py 
>>> image
<matplotlib.image.AxesImage object at 0x7f836fc249b0>
>>> dir(image)
```

| <img src="https://swcarpentry.github.io/python-novice-inflammation/fig/inflammation-01-imshow.svg" alt="heatmap" width="800"/> |
|:--:|
| *Each row in the heat map corresponds to a patient in the clinical trial dataset, and each column corresponds to a day in the dataset. Blue pixels in this heat map represent low values, while yellow pixels represent high values. As we can see, the general number of inflammation flare-ups for the patients rises and falls over a 40-day period.* |

_Observe_ that

* the patients take their medication once their inflammation flare-ups begin
* it takes around 3 weeks for the medication to take effect and begin reducing flare-ups
* and flare-ups appear to drop to zero by the end of the clinical trial.

Blue pixels in this figure (heat map) represent low values, while yellow pixels represent high values. As you can see, each object (rows) rises and falls over a 40 time unit period (columns).

Let us plot the average intensity pr. time unit.

```py
ave_value = np.mean(data, axis = 0)
ave_plot = plt.plot(ave_value)
plt.savefig('figures/ave_value.png')
plt.close()
```

Here we use the `plot()` function, which plots y versus x as lines and/or markers. Since we only supply one array, `plot()` assumes it is the _y_ or second axis variable.

Q: What happens if you do not close the figure?

For more information about `plot()` see [Pyplot tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html).


We can continue to calculate and blot descriptive statistics of our data set. Let us start with the maximum daily values - this time a little less verbose.

```py
max_plot = plt.plot(np.max(data, axis = 0))
plt.savefig('figures/max_value.png')
plt.close()
```

And then the minimum daily values.

```py
max_plot = plt.plot(np.min(data, axis = 0))
plt.savefig('figures/min_value.png')
plt.close()
```

### Grouping plots ###

`Matplotlib` allows you to group multiple plots in a single figure using subplots. With `figure()` you can create a _canvas_ to 'draw' your individual plot on. The parameter `figsize` sets the size of the canvas following the pattern `(width, height)` in inches. We are going to add three plots side by side, so approximately a 3/1 ratio (with an extra inch for y-axis labels). The method `add_subplot()` allows us to add plots to the canvas, it takes three parameters `(nrows, ncols, index)`. We write each subplot to axes variables (`axes1`, `axes2`, `axes3`). With each subplot created, we can modify plot and axis properties using the axes variables. 

Create a new file `group_plots.py` and add

```py
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='data/series-01.csv', delimiter=',')

fig = plt.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(np.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(np.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(np.min(data, axis=0))

fig.tight_layout()

plt.savefig('figures/group_plots.png')
plt.close()
```

### Visualize multiple files ###

We can use the `glob` library to find all files in a directory that match a pattern.

```sh
$ python
>>> import glob
>>> print(glob.glob('data/series*.csv'))
['data/series-02.csv', 'data/series-07.csv', 'data/series-11.csv', 'data/series-10.csv', 'data/series-12.csv', 'data/series-03.csv', 'data/series-04.csv', 'data/series-09.csv', 'data/series-06.csv', 'data/series-08.csv', 'data/series-05.csv', 'data/series-01.csv']
```

Let us combine a `glob` statement with a `for` loop to visualize multiple files. 

Create a new file `multiple_plots.py` and add

```py
import glob
import numpy as np
import matplotlib.pyplot as plt

filenames = sorted(glob.glob('data/series*.csv'))
filenames = filenames[0:3]# we only run over three files for efficiency
for filename in filenames:
    print(f'Building plot of {filename}') 

    data = np.loadtxt(fname=filename, delimiter=',')

    fig = plt.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(np.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(np.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(np.min(data, axis=0))

    fig.tight_layout()
    
    figurename = f"figures/{filename.split('/')[-1].split('.')[0]}.png"
    print(f'Storing plot as {figurename}\n---')

    plt.savefig(figurename)
    plt.close()
```

## Data Exploration with `matplotlib` and `seaborn` ##

In this lesson, we explore the [Spotify data setlesson 3](https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E22/blob/main/dat/spotify_2017.dat).

Start by reading the data into a dataframe with `pandas`

```py
import pandas as pd

df = pd.read_csv('spotify_2017.dat')
print(df.head())
```

Notice that the first column is irrelevant to our task, let us delete (`drop`) it.

```py
df.drop(df.columns[0], axis=1, inplace=True)
```

Create a _histogram_ with four attributes from Spotify: Danceability, Energy, Liveness and Acousticness. 

> **_Historgram:_** A histogram is an approximate representation of the distribution of numerical data. It is used to summarize discrete or continuous data that are measured on an interval scale. It is often used to illustrate the major features of the distribution of the data in a convenient form. The term was first introduced by Karl Pearson. To construct a histogram, the first step is to 'bin' the range of values—that is, divide the entire range of values into a series of intervals—and then count how many values fall into each interval. The bins are usually specified as consecutive, non-overlapping intervals of a variable. The bins (intervals) must be adjacent and are often (but not required to be) of equal size.


First, we create a figure 'canvas' with four subplots corresponding to our four attributes, and add labels to global axis with `text`.

```py
import matplotlib.pyplot as plt

fig, axs = plt.subplots(4, 1, figsize=(9, 9), sharex=True, dpi=150)
fig.text(0.5, 0.04, 'Score', ha='center',size=20)
fig.text(0.04, 0.5, 'Number', va='center', rotation='vertical',size=20)
```

Notice that our `axs` (axis) object is actually a `numpy` 1d array with four columns 

Second, add the histograms and subplot titles

```py
axs[0].hist(df['danceability'])
axs[0].set_title('Danceability')
axs[1].hist(df['energy'])
axs[1].set_title('Energy')
axs[2].hist(df['liveness'])
axs[2].set_title('Liveness')
axs[3].hist(df['acousticness'])
axs[3].set_title('Acousticness')
```

Lastly, we add a centered global title, show and save the figure

```py
fig.suptitle('What Makes Good Music Good?',size=20)
plt.savefig('spotify_histogram.png')
plt.show()
```

It turns out people are looking for danceability and energy, and the less acoustics and live the song is, the more popular it might be.

We tend to think that high tempo (> BMP) is more upbeat, but is that actually the case. Use a scatter plot to inspect correctaions between `tempo` and upbeat attributes: `Danceability`, `Energy`, `Liveness` and `Acousticness`.

> **_Scatter Plot:_** A scatter plot is a type of plot or mathematical diagram using Cartesian coordinates to display values for typically two variables for a set of data.

```py
fig, axs = plt.subplots(4, 1, figsize=(9, 9), sharex=True, dpi=150)
fig.text(0.5, 0.04, 'Tempo(BPM)', ha='center',size=20)   
```

Notice that we specify the _Dots per inch_ this time, which specifies the number of individual dots that can be placed in a line within the span of 1 inch. More dots means more better resolution. In academic papers, 150-300 DPIs are typically considered publication standard.

Add the scatter plot

```py
axs[0].scatter(df['tempo'], df['danceability'])
axs[0].set_title('Danceability')
axs[1].scatter(df['tempo'], df['energy'])
axs[1].set_title('Energy')
axs[2].scatter(df['tempo'], df['liveness'])
axs[2].set_title('Liveness')
axs[3].scatter(df['tempo'], df['acousticness'])
axs[3].set_title('Acousticness')
```

And show and save the scatter plot

```py
fig.suptitle('Higher BPM = More Upbeat?',size=20)
plt.savefig('bmp_correlations.png')
plt.show()
```

Suprisingly there is no correlation between those `tempo` and the upbeat attributess

You can test it with a linear model, ex

```py
from numpy.polynomial.polynomial import polyfit
x = df['tempo'].values
y = df['danceability'].values
b, m = polyfit(x, y, 1)

axs[0].plot(x, b + m * x, 'r-')
```

Finally, we can use high-level libraries that build on `matplotlib` to create publication-ready graphs. `seaborn` is a Python data visualization library based on `matplotlib` that provides a high-level interface for drawing attractive and informative statistical graphics. In other words, `seaborn` makes it easier to create fancy graphs with `matplotlib`.

Create a heatmap of the correlations between all attributes in our dataframe

```py
import seaborn as sns
corr = df.corr()
ax = plt.figure(figsize=(12,10), dpi=300)
sns.heatmap(corr,annot=True,xticklabels=corr.columns.values,yticklabels=corr.columns.values)
plt.title("Correlation of Song Attributes",size=15)
plt.tight_layout()
plt.savefig('attributes_heatmap.png')
plt.show()
```

Notice that we use `tight_layout()` to adjust the padding between and around plots.


We end by building a scatter plot matrix that plots the pairwise relationships for nine attributes

```py
df_9attrib = df[['danceability','energy','liveness',
             'acousticness','loudness','speechiness',
             'valence','tempo','duration_ms']]
ax1 = plt.figure(dpi = 300)
sns.pairplot(df_9attrib, kind = 'reg', plot_kws={'line_kws':{'color':'red'}})
plt.title("Pairplot of Song Attributes",size=15)
plt.tight_layout()
plt.savefig('attributes_splom.png')
plt.show()
```

Here we add a regression line using the `reg` parameter and color it red with the keyword argument `plot_kws`.