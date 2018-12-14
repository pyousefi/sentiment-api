from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import joblib
import time

dir_path = os.path.dirname(os.path.abspath(__file__))
CLASSIFIER = dir_path + "/res/SentimentClassifier.pkl"
VECTORIZER = dir_path + "/res/TFIDFVectorizer.pkl"


class NLPModel():

    def __init__(self, load_model=True):
        """Simple NLP
        Attributes:
            clf: sklearn classifier model
            vectorizer: TFIDF vectorizer or similar
        """
        self.clf = MultinomialNB()
        self.vectorizer = TfidfVectorizer()
        if load_model:
            self.load_model()
        self.score = None

    def load_model(self):
        self.clf = joblib.load(CLASSIFIER)
        self.vectorizer = joblib.load(VECTORIZER)

    def save_model(self):
        # file_name = "SentimentClassifier_" + time.time() + ".pkl"
        file_name = "SentimentClassifier.pkl"
        joblib.dump(self.clf, dir_path + "/res/" + file_name)

        file_name = "TFIDFVectorizer.pkl"
        joblib.dump(self.vectorizer, dir_path + "/res/" + file_name)

    def vectorizer_fit(self, X):
        """Fits a TFIDF vectorizer to the text
        """
        self.vectorizer.fit(X)

    def vectorizer_transform(self, X):
        """Transform the text data to a sparse TFIDF matrix
        """
        X_transformed = self.vectorizer.transform(X)
        return X_transformed

    def train(self, X, y):
        """Trains the classifier to associate the label with the sparse matrix
        """
        # X_train, X_test, y_train, y_test = train_test_split(X, y)
        self.clf.fit(X, y)

    def predict_proba(self, X):
        """Returns probability for the binary class '1' in a numpy array
        """
        y_proba = self.clf.predict_proba(X)
        return y_proba[:, 1]

    def predict(self, X):
        """Returns the predicted class in an array
        """
        y_pred = self.clf.predict(X)
        return y_pred
