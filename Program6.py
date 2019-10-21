from sklearn.datasets import fetch_20newsgroups #Load finenames and data from 20 newsgroups dataset
from sklearn.metrics import confusion_matrix #It is used to compute accuracy of classification
from sklearn.metrics import classification_report #Build a text report showing the main classifications metrics
import numpy as np
import os
categories=['alt.atheism','soc.religion.christian','comp.graphics','sci.med']
twenty_train=fetch_20newsgroups(subset='train',categories=categories,shuffle=True)
twenty_test=fetch_20newsgroups(subset='test',categories=categories,shuffle=True)

print("Number of Training Examples: ",len(twenty_train.data))
print("Number of Test Examples: ",len(twenty_test.data))
print(twenty_train.target_names)

from sklearn.feature_extraction.text import CountVectorizer
count_vect=CountVectorizer()
X_train_tf=count_vect.fit_transform(twenty_train.data)
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer=TfidfTransformer()
X_train_tfidf=tfidf_transformer.fit_transform(X_train_tf)
X_train_tfidf.shape

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn import metrics
mod=MultinomialNB()
mod.fit(X_train_tfidf,twenty_train.target)
X_test_tf=count_vect.transform(twenty_test.data)
X_test_tfidf=tfidf_transformer.transform(X_test_tf)
predicted=mod.predict(X_test_tfidf)

print("Accuracy: ",accuracy_score(twenty_test.target,predicted))
print(classification_report(twenty_test.target,predicted,target_names=twenty_test.target_names))
print("Confusion matrix \n",metrics.confusion_matrix(twenty_test.target,predicted))
