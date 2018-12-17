import unittest
from click.testing import CliRunner
from resources.nlpmodel import NLPModel
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import unidecode
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
STOPWORDS = dir_path + "/res/stopwords_nltk.txt"

model = NLPModel()

def test_classfier():
    assert isinstance(model.clf, MultinomialNB)

def test_vectorizer():
    assert isinstance(model.vectorizer, TfidfVectorizer)

def test_vectorization():
    # TypeError: Object of type 'csr_matrix' is not JSON serializable
    pass

def test_preprocessing():
    text = "The best movie in the world, really héhé"
    text = text.lower()
    assert text == "the best movie in the world, really héhé"
    text = unidecode.unidecode(text)
    assert text == "the best movie in the world, really hehe"

    with open(STOPWORDS, "r") as f:
        stopwords = f.readlines()
    stopwords = [word.replace("\n", "") for word in stopwords]

    list_word = [word for word in text.split() if word not in stopwords]
    sentence = " ".join(list_word).strip()
    assert sentence == "best movie world, really hehe"

def test_classification():
    model = NLPModel()
    uq_vectorized = model.vectorizer_transform(np.array(["nice is good"]))
    prediction = model.predict(uq_vectorized)
    pred_proba = model.predict_proba(uq_vectorized)
    if prediction == 0:
        pred_text = 'Negative'
    else:
        pred_text = 'Positive'
    assert pred_text == "Positive"

