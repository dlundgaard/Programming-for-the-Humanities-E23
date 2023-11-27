import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score

def evaluate_model(dataset, vectorizer, cross_validate=False):
    print(f"""Using {vectorizer} to classify {", ".join(dataset["sign"].unique())}""")
    X = vectorizer.fit_transform(dataset["horoscope-clean"]).toarray()
    y = dataset["sign"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

    classifier = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
    classifier.fit(X_train , y_train)

    y_pred = classifier.predict(X_test)

    print("\t -", f"Accuracy: {accuracy_score(y_test, y_pred):.1%}")
    print("\t -", f"True positives: {accuracy_score(y_test, y_pred, normalize=False)} from {len(X)}")
    print("\t -", f"""ROC AUC: {roc_auc_score(y_test, classifier.predict_proba(X_test), multi_class = "ovr") if dataset["sign"].nunique() > 2 else roc_auc_score(y_test, classifier.predict_proba(X_test)[:,1]):.2f}""")
    print("\t -", "Confusion matrix:", "".join(["\n\t\t" + str(row)[1:-1] for row in confusion_matrix(y_test, y_pred)]))
    if cross_validate:
        k = 10
        accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = k)
        print("\t -", f"{k}-fold Cross-validation: {accuracies.mean():.1%} ({accuracies.std() * 100:.1f}pp SD)")
    print()

if __name__ == "__main__":
    data = pd.read_csv("dat/horoscopes.csv")
    print(f"\n[INFO] found {len(data)} horoscopes\n")

    data_subset = data[data["sign"].isin(["libra", "virgo"])] # classifying only libra and virgo horoscopes (binary classification)

    evaluate_model(
        data_subset,
        CountVectorizer(),
        cross_validate = True
    )

    evaluate_model(
        data_subset, 
        CountVectorizer(stop_words = "english", max_df = 0.95), # restricting feature space, excluding stop words
        cross_validate = True
    )

    evaluate_model(
        data, # classifying all 12 signs (multiclass classfication)
        CountVectorizer()
    ) 
