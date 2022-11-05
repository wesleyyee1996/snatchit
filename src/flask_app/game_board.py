import yaml
import json
import copy
import logging

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)

class GameBoard:
  def __init__(self):
    self.logger = logging.getLogger(__name__)
    self.board_state = self.generate_game_board()
    self.tiles_in_play = {}

  def lookup_word(self, word):
    temp_tiles_in_play = copy.deepcopy(self.tiles_in_play)
    for l in word:
      if l in temp_tiles_in_play:
        temp_tiles_in_play[l] -= 1
        if temp_tiles_in_play[l] == 0:
          del temp_tiles_in_play[l]
      else:
        self.logger.info("word %s is %s"%(word, False))
        return False
    self.logger.info("word %s is %s"%(word, True))
    return True

  def get_board_state_json(self):
    return json.dumps(self.board_state, indent=4)

  def set_letter_flipped(self, letter):
    self.board_state[letter] -= 1
    if letter in self.tiles_in_play:
      self.tiles_in_play[letter] += 1
    else:
      self.tiles_in_play[letter] = 1
    self.logger.info("tiles_in_play: {}".format(self.tiles_in_play))

  def generate_game_board(self):
    board_state = {}
    with open("./letter_counts.yml", 'r') as stream:
      parsed_yml = yaml.safe_load(stream)
      for key, val in parsed_yml.items():
        board_state[key] = int(val)
      return board_state