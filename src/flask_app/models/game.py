from database.database import db

class Game(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    players = db.relationship('Player', backref='game', lazy=True)

    def __init__(self, id):
        self.id = id
