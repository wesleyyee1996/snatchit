from flask import Flask
from flask_cors import CORS
from game_board import GameBoard

app = Flask(__name__)
CORS(app)

game = GameBoard()

@app.route('/api/word/<value>')
def submit_word(value):
  isValidWord = game.lookup_word(value)
  if isValidWord:
    return 'Valid'
  return 'Invalid'

@app.route('/api/tile/<letter>', methods = ['POST'])
def letter_flipped(letter):
  game.set_letter_flipped(letter)
  print(letter)
  return game.get_board_state_json()

@app.route('/api/generateBoard')
def generate_board():
  return game.get_board_state_json()


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8000, debug=True)