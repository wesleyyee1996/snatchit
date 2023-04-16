import yaml
import json
import copy
import random
import math
from tile import Tile
from player_store import PlayerStore
from word import Word
import logging

BOARD_LEFT = 5
BOARD_RIGHT = 90


class GameBoard:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.tiles_on_board = {}  # {tile_id : Tile}
        self.num_tiles = 0
        self.player_store = PlayerStore({})
        self.generate_game_board()

    def reset(self):
        self.__init__()

    def add_player(self, player_id, player_name):
        self.player_store.add_player(player_id, player_name)

    def tiles_in_play(self):
        return [t for t in self.tiles_on_board.values() if t.is_flipped == True]

    def is_valid_word(self, word: str, tiles_to_test) -> tuple[bool, Word]:
        """
        Input:
            word: string
        Output:
            - if the word was valid: boolean
            - if the above is true, then the Word to give to the player
        """
        word_to_give_player = Word([])
        for l in word:
            letter_valid = False
            for idx, tile in enumerate(copy.deepcopy(tiles_to_test)):
                if l == tile.letter:
                    word_to_give_player.add_tile(tile)
                    tiles_to_test.pop(idx)
                    letter_valid = True
                    break
            if not letter_valid:
                self.logger.info("word %s is %s" % (word, False))
                return (False, None)

        return (True, word_to_give_player)

    def submit_word(self, word: str, player_id: int) -> bool:
        return self.take_word_from_board(word, player_id) or self.steal_word(word, player_id)

    def take_word_from_board(self, word: str, player_id: int) -> bool:
        """
        transfers tiles from board to player when a player successfully gets a word
        Args:
            word: a Word object
        """

        isValid, word_to_give_player = self.is_valid_word(
            word, self.tiles_in_play())
        if isValid:
            self.player_store.add_player_word(word_to_give_player, player_id)
            self.remove_tiles_from_board(word_to_give_player.tiles)

            return True

        return False

    def remove_tiles_from_board(self, tiles) -> None:
        for tile in tiles:
            if tile.id in self.tiles_on_board:
                del self.tiles_on_board[tile.id]

    def steal_word(self, word: str, player_id: int) -> bool:
        """
        if possible, steals a word from another player in combination with some of
        the tiles on the board
        """

        tiles_in_play = self.tiles_in_play()
        for other_player_id, other_player in self.player_store.players.items():
            if other_player_id == player_id:
                continue
            for existing_word in other_player.words:
                isValid, word_to_give_player = self.is_valid_word(
                    word, tiles_in_play + existing_word.tiles)
                if isValid:
                    other_player.remove_word(existing_word)
                    self.player_store.add_player_word(
                        word_to_give_player, player_id)
                    self.remove_tiles_from_board(word_to_give_player.tiles)
                    return True

        return False

    def get_dict_repr(self, include_tile_pos: bool = False):
        tiles_on_board = {}
        for tile_id, tile_obj in self.tiles_on_board.items():
            tiles_on_board[tile_id] = tile_obj.get_dict_repr(include_tile_pos)
        return {
            'tiles_on_board': tiles_on_board,
            'player_store': self.player_store.get_dict_repr(False)
        }

    def get_board_state_json(self):
        return json.dumps(list(self.tiles_on_board.values()), default=lambda x: x.get_json(), indent=4)

    def set_letter_flipped(self, tile_id):
        if tile_id not in self.tiles_on_board:
            raise KeyError("The tile %s is not a valid tile id" % (tile_id))
        self.tiles_on_board[tile_id].flip()

    def generate_game_board(self):
        try:
            stream = open("./letter_counts.yml", 'r')
        except FileNotFoundError as e:
            self.logger.error(e)
            stream = open("src/flask_app/letter_counts.yml", 'r')

        parsed_yml = yaml.safe_load(stream)
        for letter, count in parsed_yml.items():
            for i in range(int(count)):
                self.tiles_on_board[letter+str(i)] = Tile(letter, i)
        self.num_tiles = len(self.tiles_on_board)
        self.generate_tile_positions()

    def generate_tile_positions(self):

        def get_xy_from_index(i):
            divisor = math.floor(math.sqrt(self.num_tiles))
            x = math.floor(i/divisor)*10+random.randrange(0, 5)
            y = (i % divisor)*10+random.randrange(0, 5)
            return (x, y)

        randomized_index = list(range(0, self.num_tiles))
        random.shuffle(randomized_index)
        # self.logger.info(randomized_index)
        k = 0
        for tile_obj in self.tiles_on_board.values():
            x, y = get_xy_from_index(randomized_index[k])
            angle = random.randrange(0, 359)
            tile_obj.set_position(x, y, angle)
            # self.logger.info(tile_obj)
            k += 1
