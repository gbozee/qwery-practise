from flask import Flask,render_template,redirect,request
from src import app
from .models import TodoList
from .forms import TodoForm

@app.route('/home')
def home():
    todos = TodoList.query.all()
    return render_template("home.html",todos=todos)


@app.route('/add_todo', methods=['POST', 'GET'])
def add_todo():
    form = TodoForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            form.save()
            return redirect('/home')
    return render_template('add_todo.html', form=form)
    
@app.route('/todo/<int:todo_id>', methods=['POST', 'GET'])
def edit_todo(todo_id):
    todo = TodoList.query.get(todo_id)
    todo_form = TodoForm(obj=todo)
    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect('/home')
    return render_template('todo.html', form=todo_form, todo=todo)