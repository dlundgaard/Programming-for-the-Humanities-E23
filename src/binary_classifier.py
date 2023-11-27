import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import seaborn as sns


def plot_confusion_matrix(cm, class_names=None):
    """
    Generate a confusion matrix visualization using seaborn heatmap.

    Args:
    cm (array, shape = [n, n]): a confusion matrix of integer classes
    class_names (array, shape = [n]): String names of the integer classes
    """
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', ax=ax, cmap='Blues')

    if class_names is not None:
        ax.set_xticklabels(class_names)
        ax.set_yticklabels(class_names)

    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.savefig('figures/confusionM.png')



def main():
    data = pd.read_csv('dat/emails.csv')
    print(f'[INFO] number of documents: {data.shape[0]}')
    data.drop_duplicates(inplace=True)
    print(f'[INFO] number of documents after dedublication: {data.shape[0]}') 

    corpus = data['text']
    cv = CountVectorizer()

    X = cv.fit_transform(corpus.values).toarray()
    y = data['spam'].values

    print(f'[INFO] number of targets: {sum(y)/len(y)}')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20)

    classifier = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
    classifier.fit(X_train , y_train)

    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    class_names = ['Not Spam', 'Spam']
    plot_confusion_matrix(cm, class_names)


    print(f'Relative Accuracy; {accuracy_score(y_test, y_pred)}')
    print(f'Accuracy in instances {accuracy_score(y_test, y_pred, normalize=False)}')

    accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)    
    print(accuracies.mean())
    print(accuracies.std())

    plt.hist(accuracies, density=True, bins=30)  # density=False would make counts
    plt.xlabel('Accuracy')
    plt.ylabel('Probability')
    plt.xlabel('Data')
    plt.savefig('figures/nb_acc_dist.png')
    plt.close()

    email = [corpus[0]]
    email_array = cv.transform((email)).toarray()
    print(classifier.predict(email_array))

if __name__ == '__main__':
    main()