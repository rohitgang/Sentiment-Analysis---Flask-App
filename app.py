from flask import Flask, make_response, render_template, request
import serverFunctions as sf
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from io import BytesIO
app = Flask(__name__)

@app.route('/')
def firstOne():
   return render_template('index.html')

@app.route('/subject.html', methods= ['POST'])
def graphSubject():
    wiki= request.form['text']
    dir= sf.getSubjectivityGraph(wiki)
    return render_template('subject.html',name= 'subject', url= dir)

@app.route('/polar.html')
def graphPolar():
    dir = sf.getPolarityGraph('I hate this')
    return render_template('polar.html', name='polar', url=dir)

@app.route('/sentiment.html', methods=['GET','POST'])
def sentiment():
    if request.method == 'GET':
        return render_template('sentiment.html')
    if request.method == 'POST':
        wiki = request.form['text']
        dir = sf.getSubjectivityGraph(wiki)
        sentiment = sf.getSentiment(wiki)
        ret = 'The subjectivity is ' + str(sentiment[0]) + ' and the polarity is ' + str(sentiment[1])
        return render_template('sentimentpost.html', wiki=ret, dir= dir)


if __name__ == "__main__":
    app.run(debug= True)