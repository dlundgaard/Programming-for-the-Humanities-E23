from matplotlib import pyplot as plt
from wordcloud import WordCloud
import pandas as pd
from utils import *

def generate_wordcloud():
    dataset = pd.read_csv("horoscopes.csv")
    plt.figure(figsize = (6, 4))

    for remove_stopwords in (True, False):
        cloud = WordCloud(max_words = 100, stopwords = stopwords() if remove_stopwords else [], background_color = "white", width = 1080, height = 720).generate(" ".join(dataset["horoscope-clean"]))

        plt.imshow(cloud, interpolation="bilinear")
        plt.axis("off")
        plt.tight_layout()
        export_path = f"""wordcloud_{"no_stopwords" if remove_stopwords else "including_stopwords"}.png"""
        print(f"""[Generating wordcloud {"without" if remove_stopwords else "with"} stopwords] {export_path}""")
        plt.savefig(export_path, dpi = 200)

if __name__ == "__main__":
    generate_wordcloud()
