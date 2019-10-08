from flask import Flask
from flask_restful import Api, Resource, reqparse
from textblob import TextBlob
import matplotlib.pyplot as plt

class Sentiment(Resource):

    def getSentiment(self, wiki):
        wiki= TextBlob(wiki)
        subjectivity= wiki.sentiment.subjectivity
        polarity= wiki.sentiment.polarity
        sentiment= (subjectivity,polarity)
        return sentiment, 200

    def getSentenceAnalysis(self, wiki):
        wiki= TextBlob(wiki)
        tags= wiki.tags
        return tags, 200

    def getSentimentGraph(self, wiki):
        sentiment= getSentiment(wiki)
        subjectivity= [sentiment[0], 1-sentiment[0]]
        polarity= [sentiment[1], 1-sentiment[1]]

        subjectColors= ['yellow','blue']
        subjectPlt= plt.pie(subjectivity,
                            colors= subjectColors,
                            shadow= True)
        subjectPlt= subjectPlt.axis('equal')

        polarityColors= ['red','green']
        polarityPlt= plt.pie(polarity,
                             colors= polarityColors,
                             shadow= True)
        polarityPlt= polarityPlt.axis('equal')
        graphs= (subjectPlt, polarityPlt)
        return graphs, 200

