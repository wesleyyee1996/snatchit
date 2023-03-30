from player import Player
from word import Word
import json

class PlayerStore:
    def __init__(self):
        # self.players = {1: Player("Wesley"), 2: Player("Janice")}
        self.players = {}

    def __repr__(self):
        playersStr = ''
        for player in self.players.values():
            playersStr += str(player) + ' | '
        return playersStr
    
    def reset(self):
        # self.players = {1: Player("Wesley"), 2: Player("Janice")}
        self.players = self.__init__()

    def add_player_word(self, word: Word, player_id: int):
        self.players[player_id].add_word(word)

    def remove_player_word(self, word: Word, player_id: int):
        self.players[player_id].remove_word(word)

    def add_player(self, player_id, player_name):
        if player_id in self.players.keys():
            raise KeyError('The player %s is already added' % (self.players[player_id].name))
        self.players[player_id] = Player(player_name)

    def num_players(self):
        return len(self.players)
    
    def get_dict_repr(self):
        player_dict_repr = {}
        for player_id, player_obj in self.players.items():
            player_obj_repr = player_obj.get_dict_repr()
            player_obj_repr['id'] = player_id
            player_dict_repr[player_id] = player_obj_repr
        return {
            'players': [player_dict_repr]
        }
