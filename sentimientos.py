import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sem.logic import NegatedExpression
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize
import matplotlib.pyplot as plt
from numpy import negative, positive

analizador = SentimentIntensityAnalyzer()
sentences = open('sentiment.txt')
for sentence in sentences:
    print(sentence)
    scores = analizador.polarity_scores(sentence)
    for key in scores:
        print(key, ': ', scores[key])
        print()
dictionary= dict(scores)

listOfValues = dictionary.values()
print("Type of variable listOfValues is: ", type(listOfValues))

listOfValues = list(listOfValues)



grafic = [listOfValues[0],listOfValues[2]]
nombres = ["negativo","positivo"]
plt.pie(grafic, labels=nombres)
plt.show()

