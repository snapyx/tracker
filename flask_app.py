from flask import Flask
import tracker

app = Flask(__name__)

@app.route("/")
def welcome():
    str =  "hello thanks for choosing our service i hope it will work for you"
    return str
    
@app.route("/pnm/<number>")
def getnmloc(number):
    location = tracker.getNmLocation(number)
    return location
    