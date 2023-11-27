from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class EmailClassifier:
    def __init__(self, hidden_layer_sizes=(100,), activation='relu', solver='adam'):
        self.classifier = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, activation=activation, solver=solver)
        self.cv = CountVectorizer()
        self.X_train = self.X_test = self.y_train = self.y_test = None

    def load_data(self, filename):
        data = pd.read_csv(filename)
        data.drop_duplicates(inplace=True)
        corpus = data['text']
        self.X = self.cv.fit_transform(corpus.values).toarray()
        self.y = data['spam'].values

    def preprocess_data(self, test_size=0.2):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=test_size)

    def train(self):
        self.classifier.fit(self.X_train, self.y_train)

    def evaluate(self):
        y_pred = self.classifier.predict(self.X_test)
        cm = confusion_matrix(self.y_test, y_pred)
        print(cm)
        self.plot_confusion_matrix(cm, ['Not Spam', 'Spam'])
        print(f'Relative Accuracy: {accuracy_score(self.y_test, y_pred)}')
        print(f'Accuracy in instances: {accuracy_score(self.y_test, y_pred, normalize=False)}')

    def cross_validate(self, cv=10):
        accuracies = cross_val_score(estimator=self.classifier, X=self.X_train, y=self.y_train, cv=cv)
        print(accuracies.mean())
        print(accuracies.std())
        plt.hist(accuracies, density=True, bins=30)
        plt.xlabel('Accuracy')
        plt.ylabel('Probability')
        plt.savefig('figures/nn_acc_dist.png')
        plt.close()

    @staticmethod
    def plot_confusion_matrix(cm, class_names=None):
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt='d', ax=ax, cmap='Blues')
        if class_names is not None:
            ax.set_xticklabels(class_names)
            ax.set_yticklabels(class_names)
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        plt.savefig('figures/confusionM_ann.png')
        plt.close()

def main():
    ec = EmailClassifier()
    ec.load_data('dat/emails.csv')
    ec.preprocess_data()
    ec.train()
    ec.evaluate()
    ec.cross_validate()

if __name__ == '__main__':
    main()
