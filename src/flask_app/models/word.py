from collections import Counter
from database.database import db

class Word(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100))
    tiles = db.relationship('Tile', backref='word', lazy=True)

    def __init__(self, tiles=[]):
        self.tiles = tiles

    def __repr__(self):
        self.word = ''
        for t in self.tiles:
            self.word += t.letter
        return self.word

    def __len__(self):
        return len(self.tiles)

    def add_tile(self, tile):
        """
        Input:
          tile: a Tile object
        """
        self.tiles.append(tile)

    def tile_ids(self):
        return [t.id for t in self.tiles]

    def get_dict_repr(self, include_tile_pos: bool = False):
        tile_dict = {}
        for tile in self.tiles:
            tile_dict[tile.id] = tile.get_dict_repr(include_tile_pos)
        return tile_dict

    def list_of_letters(self):
        return [t.letter for t in self.tiles]
    
    def count_letters(self):
        return Counter(self.list_of_letters())

    def reset(self):
        self.tiles = []
