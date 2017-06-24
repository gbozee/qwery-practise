from flask import Flask,render_template
from src import app

@app.route('/home')
def home():
    todos= [
        {"title": "Want to go out", "date": "June 21st, 2017","completed":False},
        {"title": "Go to the shop", "date": "June 21st, 2017","completed":True},
        {"title": "Watch Movies", "date": "June 21st, 2017","completed":False}
    ]
    return render_template("home.html",todos=todos)


