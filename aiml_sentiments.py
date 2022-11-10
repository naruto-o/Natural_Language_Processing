# -*- coding: utf-8 -*-
"""Aiml_Sentiments.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DUVwTCsMtiQU80tYBP4PiUjvm1bTDa3g
"""

print('Sentiment Analysis')

from keras.datasets import imdb
top_words = 10000
(x_train,y_train),(x_test,y_test) = imdb.load_data(num_words = top_words)

x_train[0]

imdb.get_word_index

from keras.preprocessing import sequence

from keras.utils import pad_sequences
from keras
max_review_length = 500
x_train = sequence.pad_sequences(x_train,maxlen = max_review_length)

max_review_length = 500
x_train = sequence.pad_sequences(x_train,maxlen = max_review_length)

x_test = sequence.pad_sequences(x_test,maxlen = max_review_length)

from keras.models import Sequential
from keras.layers import Dense
from keras.layers.embeddings import Embedding
import tensorflow as tf
from keras.layers import Flatten

embedding_vector_length = 32
model1 = Sequential()
model1.add(Embedding(top_words, embedding_vector_length , input_length=max_review_length))

model1.add(Flatten())
model1.add(Dense(128, activation='relu'))
model1.add(Dense(1, activation='sigmoid'))
model1.compile(loss='binary_crossentropy', optimizer='adam', metrics= ['accuracy'])
model1.summary()

hist2 = model.fit(x_train, y_train, validation_data= (x_test, y_test), epochs = 5, batch_size= 250)

mymodel = model1.fit(x_train, y_train, validation_data= (x_test, y_test), epochs = 5, batch_size= 250)

# Commented out IPython magic to ensure Python compatibility.
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

sns.set()
acc = mymodel.history['accuracy']
val = mymodel.history['val_accuracy']
epochs = range(1,len(acc)+1)

plt.plot(epochs, acc, '-', label = 'Training Accuracy')
plt.plot(epochs, val, '-', label = 'Validation Accuracy')
plt.title('Trainig And Validation Accurcay')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.plot()

scores = model1.evaluate(x_test, y_test, verbose = 0)
print('Accuracy : {:.1%} '.format(scores[1]))

import string
import numpy as np

def analyze(text):
  translator = str.maketrans('','', string.punctuation)
  text = text.translate(translator)
  text = text.lower().split(' ')
  text = [word for word in text if word.isalpha]

  input = [1]
  for word in text:
    if word in word_dict and word_dict[word] < top_words:
      input.append(word_dict[word])
    
    else:
      input.append(2)
  padded_input = sequence.pad_sequences([input], maxlen = max_review_length)

  result = model1.predict(np.array([padded_input][0]))[0][0]
  return result

word_dict = imdb.get_word_index()
word_dict = { key:(value + 3) for key, value in word_dict.items() }
word_dict[''] = 0  # Padding
word_dict['>'] = 1 # Start
word_dict['?'] = 2 # Unknown word
reverse_word_dict = { value:key for key, value in word_dict.items() }
print(' '.join(reverse_word_dict[id] for id in x_train[0]))

analyze("i Am awesome")