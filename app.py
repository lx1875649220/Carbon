from flask import Flask,render_template
import sqlite3
import pandas as pd
#import datetime
app = Flask(__name__)

movies=pd.read_excel('movies.xlsx')

@app.route('/')
def index():
    #time=datetime.date.today()
    #return render_template("index.html",var=time)
    return render_template("index.html")


@app.route('/index')
def home():
    #return render_template("index.html")
    return index()


@app.route('/movie')
def movie():
    return render_template("movie.html",movies =movies)


@app.route('/score')
def score():
    return render_template("score.html")
#
#
@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run(debug=True)
