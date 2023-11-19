import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd
from numpy.polynomial.polynomial import polyfit
import seaborn as sns

class DataVisualizer:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.fig = None
        self.axes1 = None
        self.axes2 = None
        self.axes3 = None

    def load_data(self):
        self.data = np.loadtxt(fname=self.filename, delimiter=',')

    def create_figure(self):
        self.fig = plt.figure(figsize=(10.0, 3.0))
        self.axes1 = self.fig.add_subplot(1, 3, 1)
        self.axes2 = self.fig.add_subplot(1, 3, 2)
        self.axes3 = self.fig.add_subplot(1, 3, 3)

    def plot_average(self):
        self.axes1.set_ylabel('average')
        self.axes1.plot(np.mean(self.data, axis=0))

    def plot_max(self):
        self.axes2.set_ylabel('max')
        self.axes2.plot(np.max(self.data, axis=0))

    def plot_min(self):
        self.axes3.set_ylabel('min')
        self.axes3.plot(np.min(self.data, axis=0))

    def save_figure(self, output_filename):
        self.fig.tight_layout()
        plt.savefig(output_filename)
        plt.close()


def main():
    data = np.loadtxt(fname='dat/series/series-01.csv', delimiter=',')
    print(data)
    print(data.shape)

    image = plt.imshow(data)
    plt.savefig('figures/my_array.png')
    plt.close()
    plt.tight_layout()

    # plot average, max, min
    #data = np.loadtxt(fname='dat/series/series-01.csv', delimiter=',')

    #fig = plt.figure(figsize=(10.0, 3.0))

    #axes1 = fig.add_subplot(1, 3, 1)
    #axes2 = fig.add_subplot(1, 3, 2)
    #axes3 = fig.add_subplot(1, 3, 3)

    #axes1.set_ylabel('average')
    #axes1.plot(np.mean(data, axis=0))

    #axes2.set_ylabel('max')
    #axes2.plot(np.max(data, axis=0))

    #axes3.set_ylabel('min')
    #axes3.plot(np.min(data, axis=0))

    #fig.tight_layout()

    #plt.savefig('figures/group_plots.png')
    #plt.close()

    # as class 
    dv = DataVisualizer('dat/series/series-01.csv')
    dv.load_data()
    dv.create_figure()
    dv.plot_average()
    dv.plot_max()
    dv.plot_min()
    dv.save_figure('figures/group_plots.png')

    filenames = sorted(glob.glob('dat/series/series*.csv'))
    print(filenames)
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

    df = pd.read_csv('dat/spotify_2017.dat')
    print(df.head())
    df.drop(df.columns[0], axis=1, inplace=True)

    fig, axs = plt.subplots(4, 1, figsize=(9, 9), sharex=True, dpi=150)
    fig.text(0.5, 0.04, 'Score', ha='center',size=20)
    fig.text(0.04, 0.5, 'Number', va='center', rotation='vertical',size=20)
    axs[0].hist(df['danceability'])
    axs[0].set_title('Danceability')
    axs[1].hist(df['energy'])
    axs[1].set_title('Energy')
    axs[2].hist(df['liveness'])
    axs[2].set_title('Liveness')
    axs[3].hist(df['acousticness'])
    axs[3].set_title('Acousticness')
    fig.suptitle('What Makes Good Music Good?',size=20)
    plt.savefig('figures/spotify_histogram.png')
    
    fig, axs = plt.subplots(4, 1, figsize=(9, 9), sharex=True, dpi=150)
    fig.text(0.5, 0.04, 'Tempo(BPM)', ha='center',size=20)   
    axs[0].scatter(df['tempo'], df['danceability'])
    axs[0].set_title('Danceability')
    axs[1].scatter(df['tempo'], df['energy'])
    axs[1].set_title('Energy')
    axs[2].scatter(df['tempo'], df['liveness'])
    axs[2].set_title('Liveness')
    axs[3].scatter(df['tempo'], df['acousticness'])
    axs[3].set_title('Acousticness')
    fig.suptitle('Higher BPM = More Upbeat?',size=20)
    
    
    x = df['tempo'].values
    y = df['danceability'].values
    b, m = polyfit(x, y, 1)

    axs[0].plot(x, b + m * x, 'r-')
    plt.savefig('figures/bmp_correlations.png')
    
    
    df = pd.read_csv('dat/spotify_2017.dat')
    df.drop(df.columns[0], axis=1, inplace=True)

    print('\n build heatmap')
    print(df.describe())
    corr = df.corr(numeric_only=True)
    print(corr)
    
    ax = plt.figure(figsize=(12,10), dpi=300)
    sns.heatmap(corr,annot=True,xticklabels=corr.columns.values,yticklabels=corr.columns.values)
    plt.title("Correlation of Song Attributes",size=15)
    plt.tight_layout()
    plt.savefig('figures/attributes_heatmap.png')

    df_9attrib = df[['danceability','energy','liveness',
             'acousticness','loudness','speechiness',
             'valence','tempo','duration_ms']]
    ax1 = plt.figure(dpi = 300)
    sns.pairplot(df_9attrib, kind = 'reg', plot_kws={'line_kws':{'color':'red'}})
    plt.title("Pairplot of Song Attributes",size=15)
    plt.tight_layout()
    plt.savefig('figures/attributes_splom.png')
    



if __name__ == '__main__':
    main()