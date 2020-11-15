from flask import Flask, redirect, url_for, render_template, request
import time
import settings
import example
from example import *

#sim1Time01 = 0
#sim1Time02 = 0
#sim1TimeFinal = 0

#sim2Time01 = 0
#sim2Time02 = 0
#sim2TimeFinal = 0

app = Flask(__name__)
currentPage = "index.html"

@app.route('/')
def hello():
    return render_template("index.html")




@app.route('/sim1page1', methods= ["GET","POST"])
def sim1pg1():
    startTracking()
    settings.sim1Time01 = time.time()
    return render_template("Sim1page1.html")

@app.route('/sim1page2', methods= ["GET","POST"])
def sim1pg2():
    #print(sim1Time01)
    return render_template("Sim1page2.html")

@app.route('/sim1page3', methods= ["GET","POST"])
def sim1pg3():
    return render_template("Sim1page3.html")






@app.route('/sim2page1', methods = ["GET", "POST"])
def sim2pg1():
    #Calulations for time spent on simulation 1
    settings.sim1Time02 = time.time()
    settings.sim1TimeFinal = settings.sim1Time02 - settings.sim1Time01
   # print(sim1TimeFinal)
    settings.sim2Time01 = time.time()
    return render_template("Sim2page1.html")

@app.route('/sim2page2', methods = ["GET", "POST"])
def sim2pg2():
    return render_template("Sim2page2.html")

@app.route('/sim2page3', methods = ["GET", "POST"])
def sim2pg3():
    return render_template("Sim2page3.html")



@app.route('/results',methods = ["GET","POST"])
def resultPage():

    settings.sim2Time02 = time.time()
    settings.sim2TimeFinal = settings.sim2Time02 - settings.sim2Time01
   # print(sim2TimeFinal)
    return render_template("results.html")

@app.route('/score',methods = ["GET","POST"])
def userScores():
  #  print(sim1TimeFinal)
    return render_template("score.html", time1 = settings.sim1TimeFinal, time2 = settings.sim2TimeFinal)



if __name__ == '__main__':
    app.run(debug = True)