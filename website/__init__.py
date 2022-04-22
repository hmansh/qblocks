from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from os import path
import hashlib

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
        
        app = Flask(__name__)

        app.config['SECRET_KEY'] = 'Ni13q2w23in4AIUH5wiuHAEo231'
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)

        from .views import views
        from .api import api

        app.register_blueprint(views, url_prefix='/')
        app.register_blueprint(api, url_prefix='/')

        create_database(app)

        return app

def add_data_to_db():
        from .model import User, Vote, Position
        
        president = Position(_position="President")
        vice_president = Position(_position="Vice President")
        db.session.add(president)
        db.session.add(vice_president)
        db.session.commit()

        presidents = ['Adella Octavian', 'Gillis Lynsey', 'Mümtaz Ravinder']
        vice_presidents = ['Tad Uma', 'Rita Lucine', 'Augustus Thaddeus', 'Hendricus Esmeralda']

        for person in presidents:
                obj = Vote(_fkid=1, _name=person)
                db.session.add(obj)
                db.session.commit()

        for person in vice_presidents:
                obj = Vote(_fkid=2, _name=person)
                db.session.add(obj)
                db.session.commit()

        for i in range(0, 100):
                password = hashlib.md5('password'.encode()).hexdigest()
                obj = User(_email=f"user{i+1}@gmail.com", _password=password)
                db.session.add(obj)
                db.session.commit()

def create_database(app):
        if not path.exists('website/' + DB_NAME):
                with app.app_context():
                        db.create_all(app=app)
                        add_data_to_db()
                        print('Created Database!')