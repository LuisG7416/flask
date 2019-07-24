from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    user = {"name":"Jeffron", "favGame":"Debugger"}
    return render_template("index.html", user = user)

@app.route("/secret")
def secret():
    return render_template("secret.html")
    
@app.route("/howdy")
def howdy():
    return render_template("pensiveYeehaw.html")
    
@app.route("/sendBreakfast", methods = ["GET", "POST"])
def sendBreakfast():
    if request.method == 'GET':
        return "You didn't fill out the form. I bet you say routes weird"
    else:
        userData = dict(request.form)
        nickname = userData["nickname"][0]
        breakfast = userData["breakfast"][0]

        
        return render_template("breakfast.html", nickname = model.shout(nickname), breakfast = model.shout(breakfast) )