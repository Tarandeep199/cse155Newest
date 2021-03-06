from flask import Flask, redirect, url_for, render_template, request
import time
import settings

app = Flask(__name__)
currentPage = "index.html"

@app.route('/')
def hello():
    print("We here")
    settings.points1 = 0
    settings.points2 = 0
    return render_template("index.html")

@app.route('/sim1page1', methods= ["GET","POST"])
def sim1pg1():
    print("ok")  
    settings.points1 = settings.points1+1
    settings.sim1Time01 = time.time()
    return render_template("Sim1page1.html")

@app.route('/sim1page2', methods= ["GET","POST"])
def sim1pg2():
    settings.points1 = settings.points1+1
    return render_template("Sim1page2.html")

@app.route('/sim1page3', methods= ["GET","POST"])
def sim1pg3():
    settings.points1 = settings.points1+1
    return render_template("Sim1page3.html")


@app.route('/bufferPage', methods = ["GET", "POST"])
def buffer():
    settings.sim1Time02 = time.time()
    settings.sim1TimeFinal = round(settings.sim1Time02 - settings.sim1Time01,2)
    return render_template("buffer.html")



@app.route('/sim2page1', methods = ["GET", "POST"])
def sim2pg1():
    settings.sim2Time01 = time.time()   
    settings.points2 = settings.points2 +1

    return render_template("Sim2page1.html")

@app.route('/sim2page2', methods = ["GET", "POST"])
def sim2pg2():
    settings.points2 = settings.points2 +1
    return render_template("Sim2page2.html")

@app.route('/sim2page3', methods = ["GET", "POST"])
def sim2pg3():
    settings.points2 = settings.points2 +1
    return render_template("Sim2page3.html")



@app.route('/results',methods = ["GET","POST"])
def resultPage():
    settings.points1 = settings.points1 - 3
    settings.points2 = settings.points2 - 3
    settings.sim2Time02 = time.time()
    settings.sim2TimeFinal = round(settings.sim2Time02 - settings.sim2Time01,2)
    return render_template("results.html")

@app.route('/score',methods = ["GET","POST"])
def userScores():
  #  print(sim1TimeFinal)
    return render_template("score.html", time1 = settings.sim1TimeFinal, time2 = settings.sim2TimeFinal, pointsP1 = settings.points1, pointsP2 = settings.points2)



if __name__ == '__main__':
    app.run(debug = True)