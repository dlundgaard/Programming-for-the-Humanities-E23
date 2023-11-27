# Assignment 5: Horoscope Classification with `scikit-learn`

**Programming for the Humanities E23**

>Daniel Lundgaard 202004134@post.au.dk
>Individual submission.

In this assignment you have to use your knowledge of strings, tabular data, and machine learning to train a horoscope classifier in Python 3. 

The assignment has three problems and you you have to _solve at least two_. You should use the horoscope data available [here](https://raw.githubusercontent.com/CHCAA-EDUX/Programming-for-the-Humanities-E23/main/dat/horoscopes.csv). By default, the assignments assume that you use `scikit-learn`, but if you prefer to use another machine learning library that is a fully acceptable solution.

In your submission, please discuss what your results mean for the genre of horoscopes (what can we learn about horoscopes from the study).

## 1. Binary classification

Train a binary (two-label) Naive Bayes classifier that predicts two classes (e.g., `virgo` and `pisces`) of the `sign` variable from the horosope content of `horoscope`. Knowing that the baseline (Zero Rate) accuracy is approximately 50%, discuss the performance (accuracy and confusion matrix) of your classifier. 

**[Proposed solution](./solution.py)**

```
Using CountVectorizer() to classify virgo, libra
	 - Accuracy: 51.2%
	 - True positives: 221 from 2158
	 - ROC AUC: 0.54
	 - Confusion matrix: 
		111 111
		100 110
	 - 10-fold Cross-validation: 52.2% (2.9pp SD)
```

>The classifier only improves very slightly on the baseline accuracy, and even so, there's great variability in the performance on the testing data. In fact, 10-fold cross validation indicates that there's a ~20% probability that the classifier will perform worse than the baseline of 50% accuracy.

## 2. Effects of preprocessing

Preprocessing natural language data before training can improve classifier performance considerably. Look at the documentation for the `CountVectorizer()` function and use some of the parameters to preprocess your horoscope data. Then train two binary classifier and discuss one with and one without preprocessing and compare the performance.

**[Proposed solution](./solution.py)**

```
Using CountVectorizer() to classify virgo, libra
	 - Accuracy: 51.2%
	 - True positives: 221 from 2158
	 - ROC AUC: 0.54
	 - Confusion matrix: 
		111 111
		100 110
	 - 10-fold Cross-validation: 52.2% (2.9pp SD)

Using CountVectorizer(stop_words='english', max_df=0.95) to classify virgo, libra
	 - Accuracy: 48.8%
	 - True positives: 211 from 2158
	 - ROC AUC: 0.50
	 - Confusion matrix: 
		105 118
		103 106
	 - 10-fold Cross-validation: 53.1% (3.0pp SD)
```

>Removing stopwords, as well as restricting the vocabulary of words considered to only those occuring in less than 95% of the horoscopes, does (at least when considering the cross-validated accuracy) marginally improve predictive power. However, again, there's great variability in performance and thus uncertainty in which model will generalize better.


## 3. Multilabel Classification

Train a multilabel Naive Bayes classifier that predicts all twelve classes of the `sign` variable from the horosope content of `horoscope`. Knowing that the baseline (Zero Rate) accuracy is 8.4%, discuss the performance (accuracy and confusion matrix) of your classifier.

**[Proposed solution](./solution.py)**

```
Using CountVectorizer() to classify aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces
	 - Accuracy: 12.1%
	 - True positives: 313 from 12946
	 - ROC AUC: 0.54
	 - Confusion matrix: 
		24 21 22 19 23 19 22 19 19 15 15  9
		13 39 19 18 12 13 16  9 11 25 15  7
		10 23 22 20 20 14  8 20 22 20 19  6
		14 18 21 24 11 15 17 17 17 21 18 18
		18 23 12 15 30 16 21 12 19 20 19  9
		23 30 12 12 14 30 12 19 18 20 20 10
		17 22 20 12 20 18 24  8 18 15 22 13
		21 20 13 24 24 14 18 17 22 14 27 12
		19 20 14 18 11 17 17 12 24 23 23 13
		 9 23 14 12 15 18 10 15 16 41 18  7
		14 21 17 23 22 20 18 12 14 17 23 15
		20 36 18 27 31 12 17 18 25 19 19 15
```

>The multiclass classifier achieves a respectable prediction accuracy of around 12%, a noticeable improvement on the 8.4% base rate. However, given that horoscopes are, arguably, supposed to "uniquely" describe each group, it's not particularly promising that a classifier trained on more than 10.000 such horoscopes will only be right every 8th guess on average.
