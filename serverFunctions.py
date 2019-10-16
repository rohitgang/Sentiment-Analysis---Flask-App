import nltk
from textblob import TextBlob
import matplotlib.pyplot as plt

def getSentiment(wiki):
   wiki= TextBlob(wiki)
   subjectivity= wiki.sentiment.subjectivity
   polarity= wiki.sentiment.polarity
   sentiment= (subjectivity,polarity)
   return sentiment

def getSentenceAnalysis(wiki):
   wiki= TextBlob(wiki)
   tags= wiki.tags
   return tags

def getSubjectivityGraph(wiki):
  sentiment= getSentiment(wiki)
  subjectivity= [sentiment[0], 1-sentiment[0]]
  fig= plt.figure()
  subjectColors= ['yellow','blue']
  ax=fig.add_subplot(111)
  ax.pie(subjectivity,
        colors= subjectColors,
        shadow= True)
  ax.axis('equal')
  fig.savefig('static/images/subject.png')
  return 'static/images/subject.png'


def getPolarityGraph(wiki):
    sentiment = getSentiment(wiki)
    polarity = [sentiment[1], 1 - sentiment[1]]
    polarityColors = ['red', 'green']
    fig= plt.figure()
    ax= fig.add_subplot(111)
    ax.pie(polarity,
            colors=polarityColors,
            shadow=True)
    ax.axis('equal')
    fig.savefig('static/images/polar.png')
    return 'static/images/polar.png'