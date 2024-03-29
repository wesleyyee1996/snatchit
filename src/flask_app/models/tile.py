import math
import json
from database.database import db

class Tile(db.Model):
    id = db.Column(db.String(3), primary_key=True)
    letter = db.Column(db.String(1), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    is_flipped = db.Column(db.Boolean, nullable=False, default=False)
    pos_x = db.Column(db.Float, nullable=False)
    pos_y = db.Column(db.Float, nullable=False)
    angle = db.Column(db.Float, nullable=False)

    word_id = db.Column(db.String(50), db.ForeignKey('word.id'))
    player_id = db.Column(db.String(50), db.ForeignKey('player.id'))
    game_id = db.Column(db.String(50), db.ForeignKey('game.id'))
    
    def __init__(self, letter, number):
        self.id = letter + str(number)
        self.letter = letter
        self.number = number
        self.side_len = 6
        self.is_flipped = False

    def __repr__(self):
        return json.dumps(self.get_dict_repr(True))
    
    def set_position(self, pos_x, pos_y, angle):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.angle = angle
        self.vertices = self.get_vertices()

    def flip(self):
        self.is_flipped = True
    
    def get_dict_repr(self, include_positions: bool = False):
        data = {
            'id': self.id,
            'letter': self.letter,
            'is_flipped': self.is_flipped
        }
        if include_positions:
            data['pos_x'] = self.pos_x
            data['pos_y'] = self.pos_y
            data['angle'] = self.angle
        return data

    def get_vertices(self):
        def rotate(x, y, angle):
            angle *= math.pi/180
            xp = x * math.cos(angle) - y * math.sin(angle)
            yp = y * math.cos(angle) + x * math.sin(angle)
            return (xp, yp)

        def translate(point):
            return (round(point[0]+self.pos_x, 2), round(point[1]+self.pos_y, 2))

        vertices = [
            (0, 0),
            (0, self.side_len),
            (self.side_len, self.side_len),
            (self.side_len, 0)
        ]

        for i in range(len(vertices)):
            vertices[i] = translate(
                rotate(vertices[i][0], vertices[i][1], self.angle))

        return vertices
