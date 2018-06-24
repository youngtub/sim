import gzip
import gensim
import logging
import os
import nltk
from process import *

LOGGER = logging.getLogger('gunicorn.error')

text = open('./data/thesis.txt', 'r')
content = gensim.utils.simple_preprocess(text.read())
edited = processText(content)
print('CONTENT READY')
# model = gensim.models.Word2Vec(
#     [edited],
#     min_count=2,
#     workers=10)
# print('MODEL TRAINING')
# model.train(edited, total_examples=len(edited), epochs=10)
# model.save('./models/thesis')

model = gensim.models.Word2Vec.load('./models/thesis_sentence')
LOGGER.debug('Ready')

# bigram_transformer = gensim.models.Phrases([edited])
# smodel = gensim.models.Word2Vec(bigram_transformer[[edited]])
# smodel.save('./models/thesis_sentence')
# print('done')
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