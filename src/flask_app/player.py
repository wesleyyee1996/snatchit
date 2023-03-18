

class Player:

    def __init__(self, name):
        self.words = []
        self.points = 0
        self.name = name

    def add_word(self, word):
        self.words.append(word)
        self.add_points(len(word))

    def remove_word(self, word):
        self.words.remove(word)
        self.remove_points(len(word))

    def add_points(self, pts):
        self.points += pts

    def subtract_points(self, pts):
        self.points -= pts
