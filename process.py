import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import gensim

# nltk.download('wordnet')
# nltk.download('stopwords')
lmtzr = WordNetLemmatizer()
stopwordsList = stopwords.words('english')

def test(word):
    output = lmtzr.lemmatize(word)
    print(output)
    return output

def processText(wordList):
    lemmatized = lemmatizeNltk(wordList)
    filtered = filterStopwords(lemmatized)
    return filtered

def filterStopwords(wordList):
    output = []
    for word in wordList:
        if word not in stopwordsList:
            output.append(word)
    return output

def lemmatizeNltk(rawList):
    wordList = list(map(lambda x: lmtzr.lemmatize(x), rawList))
    return wordList

def lemmatizeGensim(list):
    return gensim.utils.lemmatize(list)