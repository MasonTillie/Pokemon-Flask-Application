from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(300), nullable=False, unique=True)
    password = db.Column(db.String(750), nullable=False)
    pokesquad_name = db.relationship('PokeSquad', backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

class PokeSquad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon1 = db.Column(db.String(150), nullable=False)
    pokemon2 = db.Column(db.String(150), nullable=False)
    pokemon3 = db.Column(db.String(150), nullable=False)
    pokemon4 = db.Column(db.String(150), nullable=False)
    pokemon5 = db.Column(db.String(150), nullable=False)
    pokemon6 = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

        # def __init__(self, pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6, user_id):
        #     pokemon_id = db.Column(db.Integer, primary_key=)
