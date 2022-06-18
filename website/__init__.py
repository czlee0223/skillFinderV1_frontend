from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
DBNAME = os.environ['DBNAME']
DBUSER = os.environ['DBUSER']
DBPASS = os.environ['DBPASS']
DBHOST = os.environ['DBHOST']


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'CZ SECRET KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DBUSER}:{DBPASS}@{DBHOST}/{DBNAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    
    from .intro import intro
    from .dashboard import dashboard
    
    app.register_blueprint(intro,url_prefix='/')
    app.register_blueprint(dashboard,url_prefix='/')
    
    return app