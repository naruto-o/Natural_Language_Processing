# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ajJ-pyamnfiqzms0F-WFh4bqtgjVrR_7
"""

import os 
import nltk.corpus
print(os.listdir(nltk.data.find("corpora")))
from nltk.corpus import brown
w = brown.words()
for i in w[:500]:
  print(i,end = " ")

from nltk.corpus import gutenberg
print(gutenberg.fileids())