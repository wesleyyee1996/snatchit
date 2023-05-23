import yaml
import json
import random
import math
import os
from tile import Tile
from player_store import PlayerStore
from word import Word
import logging
import importlib  
merriam_webster_api = importlib.import_module("merriam-webster-api.merriam_webster.api")
CollegiateDictionary = merriam_webster_api.CollegiateDictionary
WordNotFoundException = merriam_webster_api.WordNotFoundException
#from merriam_webster_api.merriam_webster.api import (CollegiateDictionary,
                                                     #WordNotFoundException)
import exceptions

BOARD_LEFT = 5
BOARD_RIGHT = 90
MIN_WORD_LENGTH = 4


class GameBoard:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.tiles_on_board = {}  # {tile_id : Tile}
        self.num_tiles = 0
        self.player_store = PlayerStore({})
        self.set_dictionary_api_key()
        self.generate_game_board()

    def reset(self):
        self.__init__()

    def set_dictionary_api_key(self):
        college_key = (os.getenv("MERRIAM_WEBSTER_COLLEGIATE_KEY"))
        self.dictionary_api_key = college_key
        self.collegiate_dictionary = CollegiateDictionary(
            self.dictionary_api_key)

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
            matching_tiles = [
                tile for tile in tiles_to_test if tile.letter == l]
            if not matching_tiles:
                self.logger.info(f"word {word} is {False}")
                return False, None
            tile_to_remove = matching_tiles[0]
            tiles_to_test.remove(tile_to_remove)
            word_to_give_player.add_tile(tile_to_remove)
        return True, word_to_give_player

    def lookup_word(self, word: str):
        try:
            defs = [(entry.word, entry.function, definition) for entry in self.collegiate_dictionary.lookup(word)
                    for definition, examples in entry.senses]
        except WordNotFoundException:
            raise exceptions.WordDoesNotExistInDictionaryException(word)
        first_def = defs[0]
        return f"{first_def[0]} [{first_def[1]}]: {first_def[2]}"

    def submit_word(self, word: str, player_id: int) -> bool:
        if len(word) < MIN_WORD_LENGTH:
            raise exceptions.WordIsTooShortException(word, MIN_WORD_LENGTH)
        isValid, word_to_give_player = self.is_valid_word(
            word, self.tiles_in_play())
        isStolen = self.steal_word(word, player_id)
        if not isValid and not isStolen:
            raise exceptions.CannotMakeWordFromGameTilesException(word)

        definition = self.lookup_word(word)
        if not isStolen:
            self.take_word_from_board(word_to_give_player, player_id)
        return definition

    def take_word_from_board(self, word_to_give_player: Word, player_id: int) -> bool:
        """
        transfers tiles from board to player when a player successfully gets a word
        Args:
            word: a Word object
        """
        self.player_store.add_player_word(word_to_give_player, player_id)
        self.remove_tiles_from_board(word_to_give_player.tiles)

    def remove_tiles_from_board(self, tiles) -> None:
        for tile in tiles:
            if tile.id in self.tiles_on_board:
                del self.tiles_on_board[tile.id]

    def steal_word(self, word: str, player_id: int) -> bool:
        """
        if possible, steals a word from another player in combination with some of
        the tiles on the board
        """

        def is_existing_word_subset_of_word_to_give(word_to_give_player, existing_word):
            for tile in existing_word.list_of_letters():
                if tile in word_to_give_player.count_letters():
                    word_to_give_player.count_letters()[tile] -= 1
                    if word_to_give_player.count_letters()[tile] == 0:
                        del word_to_give_player.count_letters()[tile]
                else:
                    return False
            return True

        tiles_in_play = self.tiles_in_play()
        for player in self.player_store.players.values():
            for existing_word in player.words:
                isValid, word_to_give_player = self.is_valid_word(
                    word, tiles_in_play + existing_word.tiles)
                # if word_to_give_player contains all of existing_word tiles
                if isValid and is_existing_word_subset_of_word_to_give(word_to_give_player, existing_word):
                    player.remove_word(existing_word)
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
