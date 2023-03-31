import json
from word import Word

class Player:

    def __init__(self, name):
        self.words = [] # list of Word objects
        self.points = 0
        self.name = name

    def __repr__(self):
        return json.dumps(self.get_dict_repr())

    def add_word(self, word: Word):
        self.words.append(word)
        self.add_points(len(word))

    def remove_word(self, word: Word):
        self.words.remove(word)
        self.subtract_points(len(word))

    def add_points(self, pts):
        self.points += pts

    def subtract_points(self, pts):
        self.points -= pts

    def get_dict_repr(self, include_tile_pos: bool = False):
        return {
            'name': self.name,
            'points': self.points,
            'words': [x.get_dict_repr(include_tile_pos) for x in self.words]
        }
    
    def reset(self):
        self.__init__(self.name)
