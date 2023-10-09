# Assignment 2: Word Importance #

In this assignement you have to work with `horoscope.csv` in order to learn how to identify important words (keywords and concepts) in a data set. The assignment will require you to combine your basic understanding of programming with python (control flow, functions, lists) with a string manipulation task inspired by information retrieval. You only have to solve two out of three problems, but if you feel up to it, go for all three.

You can download the `horoscope.csv` file [HERE](https://raw.githubusercontent.com/CHCAA-EDUX/Programming-for-the-Humanities-E23/main/dat/horoscopes.csv).

## Format ##

For your assignment you should submit a separate report in Markdown combined with py scripts for your code.


### Submission ###

Again, two options a) text report in pdf accompanied by Python scripts OR b) markdown with text and Python code blocks. __Please remember to hand in individual assignments even though you have developed you solution in a group__. The final exam, that is, your portfolio, should reflect your individual solution. Submit through Brightspace (either files or link to a public GitHub repository).

## Prerequisites ##

For the assignment, you need to load data from `horoscope.csv` available through [GitHub](https://raw.githubusercontent.com/CHCAA-EDUX/Programming-for-the-Humanities-E23/main/dat/horoscopes.csv). 


We will use the `pandas` library to load the csv in Python. If `pandas` is not installed in your environment, that is, if you get this result from Python:

```py
>>> import pandas
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pandas'
```

You need to install it from the terminal

```sh
$ pip3 install pandas
```

To load the file in Python do the following:

```py
import pandas as pd
df = pd.read_csv('horoscopes.csv')
```

Assuming that you `horoscope.csv` file is in the same directory as your script. If your file is in another directory, ex. 'data/', you need to include the relative path:

```py
import pandas as pd # import pandas module
df = pd.read_csv('data/horoscopes.csv') # assign the dataframe with your data to variable 'df'
```

Csv files are tabular data (e.g., spreadsheets) and the horoscopes to be analyzed are in the `'horoscope-clean'` column. To extract that column and put it in the variable `texts` as a list data type use the following statement

```py
texts = df['horoscope-clean'].values
```

To test if you have extracted the data correctly, you can check the length of the list:

```py
print(len(texts))
```

Which should return `12946`, meaning that you have 12946 horoscopes. If you print the first element in the list, `print(texts[0])`, you should see that (notice that there are no punctuation):

```sh
You re not the sort to play safe and even if you have been a bit more cautious than usual in recent weeks you will more than make up for it over the next few days Plan your new adventure today and start working
on it tomorrow
```

## Problem 1: With or without function words ##

Compare the top 100 most frequent words in all horoscopes with and without stopwords (i.e. function words), what seems to be the most striking differences? You should include your stopword list (or a link to) in the answer. You can use a wordcloud to visualize the comparison (requires that you `pip install wordcloud` from the terminal). 

```py
from wordcloud import WordCloud
import matplotlib.pyplot as plt
wordcloud = WordCloud(stopwords=stopwordlist,background_color="white").generate(texts)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout()
plt.savefig('wordcloud.png')
```

or you can use the following set functions to compare lists of words:

```py

def intersection(lst1, lst2):
    """ returns the intersection between two lists
    e.g., lst1 = [1,2,3] and lst2 = [2,3,4], then the intersection is [2,3]
    """
    return list(set(lst1) & set(lst2))

def difference(lst1, lst2):
    """ returns the asymmetric difference between two lists
    e.g., lst1 = [1,2,3] and lst2 = [2,3,4], the the difference (for lst1) is [1]
    """
    return list(set(lst1).difference(set(lst2)))
```

## Problem 2: Sign-specific indexing ##

Compare top 200 most frequent words for at least three different Zodiac signs (ex. virgo, leo, pisces) using the `difference` set function from Problem 1. Are there any apparent characteristics/distinct differences between the signs?

To extract subsets of the data based on a specific zodiac sign, use the following indexing technique. First select the relevant sign:

```py
signs = list(set(df['sign'].values))
print(signs)
```

Which should result in the following lists

```sh
['libra', 'virgo', 'taurus', 'capricorn', 'aquarius', 'pisces', 'leo', 'gemini', 'scorpio', 'sagittarius', 'aries', 'cancer']
```

To extract horoscopes from 'virgo' use boolean indexing in the dataframe column `horoscope-clean`

```py
idxs = df['sign'] == 'virgo'
texts = df['horoscope-clean'].loc[idxs].values
```

Or for 'pisces' use

```py
idxs = df['sign'] == 'pisces'
texts = df['horoscope-clean'].loc[idxs].values
```

## Problem 3: Document similarity ##

Generate a document-term matrix from the horoscope data and extract $n$ documents, where $n > 5$. Compute the similarity between all extracted documents and, in natural langauge, explain the extrema (the similarity between the two least and two most similar documents). You can find the necessary functionality in `word_importance.py` [HERE](https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E23/blob/main/src/word_importance.py).