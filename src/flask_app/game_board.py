import yaml
import json
import copy
import logging
import random
import math
from tile import Tile
from player_store import PlayerStore

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)

BOARD_LEFT = 5
BOARD_RIGHT = 90


class GameBoard:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.board_state = {}
        self.tiles_in_play = {}
        self.tile_positions = []
        self.num_tiles = 0
        self.player_store = PlayerStore()
        self.generate_game_board()

    def lookup_word(self, word):
        temp_tiles_in_play = copy.deepcopy(self.tiles_in_play)
        for l in word:
            if l in temp_tiles_in_play:
                temp_tiles_in_play[l] -= 1
                if temp_tiles_in_play[l] == 0:
                    del temp_tiles_in_play[l]
            else:
                self.logger.info("word %s is %s" % (word, False))
                return False
        self.logger.info("word %s is %s" % (word, True))
        return True

    def get_board_state_json(self):
        return json.dumps(self.tile_positions, default=lambda x: x.get_json(), indent=4)

    def set_letter_flipped(self, letter):
        self.board_state[letter] -= 1
        if letter in self.tiles_in_play:
            self.tiles_in_play[letter] += 1
        else:
            self.tiles_in_play[letter] = 1
        self.logger.info("tiles_in_play: {}".format(self.tiles_in_play))

    def generate_game_board(self):
        with open("./letter_counts.yml", 'r') as stream:
            parsed_yml = yaml.safe_load(stream)
            for key, val in parsed_yml.items():
                self.board_state[key] = int(val)
                self.num_tiles += int(val)
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
        for letter, num in self.board_state.items():
            for i in range(num):
                x, y = get_xy_from_index(randomized_index[k])
                angle = random.randrange(0, 359)
                tile = Tile(letter, i, x, y, angle)
                self.tile_positions.append(tile)
                self.logger.info(tile)
                k += 1

    # def generate_tile_positions(self):
    #     for letter, num in self.board_state.items():
    #         for i in range(num):
    #             tile = self.get_random_tile_pos(letter, num)
    #             while not self.valid_tile_position(tile):
    #                 tile = self.get_random_tile_pos(letter, num)
    #                 self.logger.info(tile)
    #             self.tile_positions.append(tile)

    def get_random_tile_pos(self, letter, num):
        px = random.randrange(BOARD_LEFT, BOARD_RIGHT)
        py = random.randrange(BOARD_LEFT, BOARD_RIGHT)
        angle = random.randrange(0, 359)
        return Tile(letter, num, px, py, angle)

    def valid_tile_position(self, tile):
        for existing_tile in self.tile_positions:
            if self.tiles_overlap(tile, existing_tile):
                return False
        return True

    def tiles_overlap(self, tile1, tile2):
        a = tile1.vertices
        b = tile2.vertices
        polygons = [a, b]

        for i in range(len(polygons)):
            polygon = polygons[i]
            for i1 in range(len(polygon)):
                i2 = (i1 + 1) % len(polygon)
                p1 = polygon[i1]
                p2 = polygon[i2]

                normal = {'x': p2[1] - p1[1], 'y': p1[0] - p2[0]}

                minA = maxA = None
                for j in range(len(a)):
                    projected = normal['x'] * a[j][0] + normal['y'] * a[j][1]
                    if (not minA or projected < minA):
                        minA = projected
                    if (not maxA or projected > maxA):
                        maxA = projected

                minB = maxB = None
                for j in range(len(b)):
                    projected = normal['x'] * b[j][0] + normal['y'] * b[j][1]
                    if (not minB or projected < minB):
                        minB = projected
                    if (not maxB or projected > maxB):
                        maxB = projected

                if (maxA < minB or maxB < minA):
                    return False
        return True
