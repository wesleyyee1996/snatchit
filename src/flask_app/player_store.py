from player import Player


class PlayerStore:
    def __init__(self):
        self.players = {1: Player("Wesley"), 2: Player("Janice")}

    def add_player_word(self, word, player_id):
        self.players[player_id].add_word(word)

    def remove_player_word(self, word, player_id):
        self.players[player_id].remove_word(word)
