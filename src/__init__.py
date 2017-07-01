import os
from flask import Flask
from .models import db
from flask_migrate import Migrate

app = Flask(__name__, template_folder='templates', static_folder='static')

FLASK_CONFIGURATION  = os.getenv('FLASK_CONFIGURATION', 'settings/local.py')
app.config.from_pyfile(FLASK_CONFIGURATION)

if FLASK_CONFIGURATION == 'settings/local.py':
    from flask_debugtoolbar import DebugToolbarExtension
    DebugToolbarExtension(app)

migrate = Migrate(app, db)

db.init_app(app)

def create_tables():
    db.create_all()

from . import views