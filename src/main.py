from flask import Flask,render_template

app = Flask(__name__)

@app.route('/home')
def result():
    todos= [
        {"ID": 1,"title": "Want to go out", "uncompleted":False},
        {"ID": 2,"title": "Go to the shop", "uncompleted":False},
        {"ID": 3,"title": "Watch Movies", "uncompleted":False} ]
    return render_template("home.html",todos=todos)


