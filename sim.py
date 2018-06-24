import gzip
import gensim
import logging
import os
import nltk
from process import *

text = open('./data/bible.txt', 'r')
content = gensim.utils.simple_preprocess(text.read())
edited = processText(content)

model = gensim.models.Word2Vec(
    [edited],
    min_count=2,
    workers=10)

model.train(content, total_examples=len(content), epochs=10)

def similarToWord(word):
    output = model.wv.most_similar(positive=word, topn=30)
    return output

def similarityBetweenTwoWords(word1, word2):
    output = model.wv.similarity(w1=word1, w2=word2)
    return output

def getVector(word):
    vector = model.wv.get_vector(word)
    return vector

def wordsCloserThan(word, comparison):
    closerThan = model.wv.words_closer_than(word, comparison)
    return closerThan

def oddOneOut(words):
    doesntMatch = model.wv.doesnt_match(words)
    return doesntMatch

def getDistinceBetweenEntitys(entity1, entity2):
    distance = model.wv.distance(entity1, entity2)
    return distance

def getArraySimilarity(array1, array2):
    nSim = model.wv.n_similarity(array1, array2)
    return nSim




# similarToWord("ronaldo")
# similarityBetweenTwoWords("ronaldo", "father")