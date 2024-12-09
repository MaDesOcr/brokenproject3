from sqlalchemy import SQLAlchemy

db = SQLAlchemy

class User():
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Game():
    title = db.Column(db.String(120), nullable=False)
    genre = db.Column(db.String(80), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    developer_id = db.Column(db.Integer, db.ForeignKey('developer.id'), nullable=False)
    developer = db.relationship('Developer', backref='games')

class Developer():
    name = db.Column(db.String(120), nullable=False)
    founded = db.Column(db.Integer, nullable=False)
    headquarters = db.Column(db.String(120), nullable=False)

class Platform():
    name = db.Column(db.String(80), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)

class Review():
    game = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    reviews = db.relationship('Game', backref='reviews')
    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.Text, nullable=True)
    reviewer_name = db.Column(db.String(120), nullable=False)
