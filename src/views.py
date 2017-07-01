from flask import Flask,flash,render_template,redirect,request,session, url_for
from flask_login import LoginManager, login_required, login_user
from src import app
from .models import User
from .forms import TodoForm, LoginForm

login_manager = LoginManager()
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id==user_id)

@app.route('/home')
def home():
    todos= [
        {"title": "Want to go out", "date": "June 21st, 2017","completed":False},
        {"title": "Go to the shop", "date": "June 21st, 2017","completed":True},
        {"title": "Watch Movies", "date": "June 21st, 2017","completed":False}
    ]
    return render_template("home.html",todos=todos)


@app.route('/add_todo', methods=['POST', 'GET'])
@login_required
def add_todo():
    form = TodoForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            form.save()
            return redirect('/home')
    return render_template('add_todo.html', form=form)

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



