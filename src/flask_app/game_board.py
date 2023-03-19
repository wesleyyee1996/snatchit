import yaml
import json
import copy
import logging
import random
import math
from tile import Tile
from player_store import PlayerStore
from word import Word

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)

BOARD_LEFT = 5
BOARD_RIGHT = 90

class GameBoard:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.tiles_on_board = {} # {tile_id : Tile}
        self.num_tiles = 0
        self.player_store = PlayerStore()
        self.generate_game_board()

    def __filter_on_flipped(self, pair):
        __, tile_obj = pair
        if tile_obj.is_flipped == True:
            return True
        return False

    def is_valid_word(self, word):
        """
        Input:
            word: string
        Output:
            - if the word was valid: boolean
            - if the above is true, then the Word to give to the player
        """
        tiles_in_play = [t for t in self.tiles_on_board.values() if t.is_flipped == True]
        # self.logger.info('test', tiles_in_play)
        word_to_give_player = Word()
        for l in word:
            for idx, tile in enumerate(copy.deepcopy(tiles_in_play)):
                if l == tile.letter:
                    word_to_give_player.add_tile(tile)
                    tiles_in_play.pop(idx)
                else:
                    self.logger.info(self.logger.info("word %s is %s" % (word, False)))
                    return (False, None)

        # self.logger.info("word %s is %s" % (word, True))
        return (True, word_to_give_player)
    
    def take_word_from_board(self, word, player_id):
        """
        transfers tiles from board to player when a player successfully gets a word
        Args:
            word: a Word object
        """

        isValid, word_to_give_player = self.is_valid_word(word)
        if isValid:
            self.player_store.add_player_word(word_to_give_player, player_id)
            for tile in word_to_give_player.tiles:
                del self.tiles_on_board[tile.id]

            return (isValid, word_to_give_player.tile_ids())
        
        return (False, [])


    def get_board_state_json(self):
        return json.dumps(list(self.tiles_on_board.values()), default=lambda x: x.get_json(), indent=4)

    def set_letter_flipped(self, tile_id):
        self.tiles_on_board[tile_id].flip()

    def generate_game_board(self):
        with open("./letter_counts.yml", 'r') as stream:
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
        self.logger.info(randomized_index)
        k = 0
        for tile_obj in self.tiles_on_board.values():
            x, y = get_xy_from_index(randomized_index[k])
            angle = random.randrange(0, 359)
            tile_obj.set_position(x,y,angle)
            self.logger.info(tile_obj)
            k += 1
