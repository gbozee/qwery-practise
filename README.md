# Qwery To-do List App
Qwery To-do List App lets you create a list of todos and keep track of your completed and uncompleted tasks. With this app, you can create, edit and delete todos

## Getting Started
Clone the repository to your local machine
```
git clone https://github.com/gbozee/qwery-practise.git
```
### Prerequisites

You should have [Python 3.6.1](https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe) installed.
After installation, install the following dependencies  on your local machine using pip by 

```
pip install -r requirements/base.txt
```

# qwery-practice

This project is about applying all that we have learnt in the 6 weeks of learning.

We would be implementing a Todo application which would consist of the following pages
* A home page that displays the list of todos and a link to add a new todo
* A add-todo page which is where a todo is added
* A login page which is where a user can choose to signup/login
* A detail view for each todo 

Things to not out for.
On the home page, when the user isn't authenticated, A link at the top of the page to login/signup a user
if a user is already logged in, then instead of the login/signup link, he sees his/her name at the top left of the screen

Also on the home page, There exists a list of todos that do not belong to anyone if the user hasn't logged in. Below the list of todos is a button to add a new todo that takes the user to the add-todo page to add a todo.

If no todos exists, an message, Be the first person to add a todo should be displayed.

Also if a user is logged in, The list of todos that show up are only todos that were created by the user. 

On each todo in the todo list, a link on the todo to go to the detail page.

On the detail page of each todo. The todo detail and a button to mark as completed.

