import unittest
from click.testing import CliRunner
from resources.nlpmodel import NLPModel
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

model = NLPModel()

def test_classfier():
    assert isinstance(model.clf, MultinomialNB)

def test_vectorizer():
    assert isinstance(model.vectorizer, TfidfVectorizer)

def test_vectorization():
    # TypeError: Object of type 'csr_matrix' is not JSON serializable
    pass

# def test_classification():
#     model = NLPModel()
#     uq_vectorized = model.vectorizer_transform(np.array(["nice is good"]))
#     prediction = model.predict(uq_vectorized)
#     pred_proba = model.predict_proba(uq_vectorized)
#     if prediction == 0:
#         pred_text = 'Negative'
#     else:
#         pred_text = 'Positive'
#     assert pred_text == "Positive"

    # No confidence test as it can change with model retraining

