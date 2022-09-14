from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(300), nullable=False)
    last_name = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(300), nullable=False, unique=True)
    password = db.Column(db.String(750), nullable=False)
    pokesquad_name = db.relationship('PokeSquad', backref='author', lazy=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

        class PokeSquad(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            pokemon1 = db.Column(db.String(150), nullable=False)
            pokemon2 = db.Column(db.String(150), nullable=False)
            pokemon3 = db.Column(db.String(150), nullable=False)
            pokemon4 = db.Column(db.String(150), nullable=False)
            pokemon5 = db.Column(db.String(150), nullable=False)
            pokemon6 = db.Column(db.String(150), nullable=False)
            date_created = db.Column(db.DateTime, nullable=False, defualt=datetime.utcnow)
        #     user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable=False)

        # def __init__(self, pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6, user_id):
        #     pokemon_id = db.Column(db.Integer, primary_key=)
