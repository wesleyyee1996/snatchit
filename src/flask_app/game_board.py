import yaml
import json
import copy

class GameBoard:
  def __init__(self):
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
        return False
    return True

  def get_board_state_json(self):
    return json.dumps(self.board_state, indent=4)

  def set_letter_flipped(self, letter):
    self.board_state[letter] -= 1

  def generate_game_board(self):
    board_state = {}
    with open("./letter_counts.yml", 'r') as stream:
      parsed_yml = yaml.safe_load(stream)
      for key, val in parsed_yml.items():
        board_state[key] = int(val)
      return board_state