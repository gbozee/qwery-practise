# Qwery To-do List App
Qwery To-do List App lets you create a list of todos and keep track of your completed and uncompleted tasks. With this app, you can create, edit and delete todos. 

## Getting Started
Clone the repository to your local machine
```
git clone https://github.com/gbozee/qwery-practise.git
```
### Prerequisites

* You should have [Python 3.6.1](https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe) installed.
* After installation, install the Flask web framework and other dependencies on your local machine using pip:

_For developers_
```
pip install -r requirements/local.txt
```
_In production_
```
pip install -r requirements/production.txt
```

### Running the app
1. Set the environmental variables using the commands
```
export FLASK_APP=src/__init__.py
export FLASK_DEBUG=1
```
2. Run the command `flask run` and go to 127.0.0.1:5000 on your web browser if you are running it on your local machine

## Things to work on 
On the home page, when the user isn't authenticated, A link at the top of the page to login/signup a user
if a user is already logged in, then instead of the login/signup link, he sees his/her name at the top left of the screen

Also on the home page, There exists a list of todos that do not belong to anyone if the user hasn't logged in. Below the list of todos is a button to add a new todo that takes the user to the add-todo page to add a todo.

If no todos exists, an message, Be the first person to add a todo should be displayed.

Also if a user is logged in, The list of todos that show up are only todos that were created by the user. 

On each todo in the todo list, a link on the todo to go to the detail page.

On the detail page of each todo. The todo detail and a button to mark as completed.

## Contributors
* [yemisi-o](www.github.com/yemisi-o)
* [tmosco](www.github.com/tmosco)
* [gbozee](www.github.com/gbozee)
* [oagbaneje](www.github.com/oagbaneje)

