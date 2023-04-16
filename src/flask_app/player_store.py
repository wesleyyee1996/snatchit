from player import Player
from word import Word
import json
import logging


class PlayerStore:
    def __init__(self, players={}):
        self.logger = logging.getLogger(__name__)
        # self.players = {1: Player("Wesley"), 2: Player("Janice")}
        self.logger.info("Resetting player store")
        self.players = players

    def __repr__(self):
        playersStr = ''
        for player in self.players.values():
            playersStr += str(player) + ' | '
        return playersStr

    def reset(self):
        # self.players = {1: Player("Wesley"), 2: Player("Janice")}
        self.logger.info("Resetting player store reset")
        self.players = self.__init__()

    def add_player_word(self, word: Word, player_id: int):
        self.players[player_id].add_word(word)

    def remove_player_word(self, word: Word, player_id: int):
        self.players[player_id].remove_word(word)

    def num_players(self):
        return len(self.players)

    def get_dict_repr(self, include_tile_pos: bool = False):
        player_dict_repr = {}
        for player_id, player_obj in self.players.items():
            player_obj_repr = player_obj.get_dict_repr(include_tile_pos)
            player_obj_repr['id'] = player_id
            player_dict_repr[player_id] = player_obj_repr
        return {
            'players': player_dict_repr
        }

    def add_player(self, player_id: int, player_name: str):
        if player_id in self.players:
            raise KeyError(
                "Player w/ ID: %s and name %s is already present" % (player_id, player_name))
        self.logger.info('added player %s' % (player_id))
        new_player = Player(player_name)
        self.players[player_id] = new_player
