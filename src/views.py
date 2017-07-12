from flask import Flask,render_template,redirect,request,flash
from src import app
from .models import TodoList
from .forms import TodoForm

@app.route('/')
@app.route('/home')
def home():
    todos = TodoList.query.all()
    todos_done = TodoList.query.filter_by(status=True)
    todos_undone = TodoList.query.filter_by(status=False)
    return render_template("home.html",todos=todos, todos_done=todos_done, todos_undone=todos_undone)


@app.route('/add_todo', methods=['POST', 'GET'])
def add_todo():
    form = TodoForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            form.save()
            flash('Your todo has been added successfully!')
            return redirect('/home')
    return render_template('add_todo.html', form=form)
    
@app.route('/edit_todo/<int:todo_id>', methods=['POST', 'GET'])
def edit_todo(todo_id):
    todo = TodoList.query.get_or_404(todo_id)
    todo_form = TodoForm(obj=todo)
    if request.method == 'POST':
        if todo_form.validate_on_submit():
            if request.form["btn"] == "Update":
                todo_form.update(todo)
                flash('Your todo has been updated successfully!')
            else:
                todo_form.delete(todo)
                flash('Your todo has been deleted successfully!')
            return redirect('/home')
    return render_template('edit_todo.html', form=todo_form, todo=todo)