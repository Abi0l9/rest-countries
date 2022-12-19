import os
from flask_sqlalchemy import SQLAlchemy



basedir = os.path.abspath(os.path.dirname(__file__))
database_path = 'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy()

def setup_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

class Country(db.Model):
    __tablename__= 'country'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    population = db.Column(db.Integer)
    currency = db.Column(db.String(100))
    official_language = db.Column(db.String(100))
    cca3 = db.Column(db.String(50))

    def __repr__(self):
        return f"{self.name}"