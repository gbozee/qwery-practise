from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from src import app
from .models import TodoList, User
from .forms import TodoForm, LoginForm, SignupForm

login_manager = LoginManager()
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()


@app.route('/')
@app.route('/home')
def home():
    # Added to pass ToDoForm to the Add ToDo modal on the homepage
    form = TodoForm()

    todos = TodoList.query.all()
    user = current_user.get_id()  # you didn't check if the user is logged in
    user_todos = []
    if user:
        # th euser here is a string/integer not a user object
        user = User.query.get(user)
        user_todos = user.todolists.all()
    todos_done = TodoList.query.filter_by(status=True)
    todos_undone = TodoList.query.filter_by(status=False)
    return render_template("home.html", todos=todos, todos_done=todos_done, todos_undone=todos_undone, form=form)


@app.route('/add_todo', methods=['POST', 'GET'])
@login_required
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


@app.route("/login/", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.get_user()
        login_user(user)
        flash('Logged in successfully.', "success")
        next_ = request.args.get('next')

        return redirect(next_ or url_for('home'))
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out.", "info")
    return redirect(url_for('home'))


@app.route("/signup/", methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        form.save()
        return redirect('/login')
    return render_template('signup.html', form=form)
