from flask import Flask,render_template,redirect,request
from src import app
from .forms import TodoForm

@app.route('/home')
def home():
    todos= [
        {"title": "Want to go out", "date": "June 21st, 2017","completed":False},
        {"title": "Go to the shop", "date": "June 21st, 2017","completed":True},
        {"title": "Watch Movies", "date": "June 21st, 2017","completed":False}
    ]
    return render_template("home.html",todos=todos)


@app.route('/add_todo', methods=['POST', 'GET'])
def add_todo():
    form = TodoForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            form.save()
            return redirect('/home')
    return render_template('add_todo.html', form=form)
    
