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
        self.add_points(len(word)-3)

    def remove_word(self, word: Word):
        self.words.remove(word)
        self.subtract_points(len(word)-3)

    def add_points(self, pts):
        self.points += pts

    def subtract_points(self, pts):
        self.points -= pts

    def get_dict_repr(self, include_tile_pos: bool = False):
        word_dict = {}
        for word in self.words:
            word_dict[str(word)] = word.get_dict_repr(include_tile_pos)
        return {
            'name': self.name,
            'points': self.points,
            'words': word_dict
        }
    
    def reset(self):
        self.__init__(self.name)
