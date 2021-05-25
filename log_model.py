import pandas as pd
import numpy as np
import utilities as utils
#import re
#import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

articles_df = pd.read_csv("articles-web.csv", index_col=0)
articles_df = articles_df.dropna()
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(articles_df.clean_text)
y = articles_df.is_fake
X_train_validate, X_test, y_train_validate, y_test = train_test_split(X, y, stratify=y, test_size=.2)
X_train, X_validate, y_train, y_validate = train_test_split(X_train_validate, y_train_validate, stratify=y_train_validate, test_size=.3)
lm = LogisticRegression().fit(X_train, y_train)

def log_model(text):
    text = tfidf.transform([text])
    prediction = lm.predict(text)
    probability = lm.predict_proba(text)
    return prediction[0], probability