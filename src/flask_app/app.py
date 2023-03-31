from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_classful import FlaskView, route
from game_board import GameBoard
import json

app = Flask(__name__)
CORS(app)

class SnatchItApp(FlaskView):
    route_base = '/'
    route_prefix = '/api/'

    def __init__(self):
        self.game = GameBoard()

    @route('/tile')
    def tile(self):
        tile_id = request.args.get('tile_id', None)
        self.game.set_letter_flipped(tile_id)
        return json.dumps({'game_state': self.game.get_dict_repr(include_tile_pos = False)})
    
    @route('/word')
    def word(self):
        word = request.args.get('word', None)
        player_id = int(request.args.get('player_id', None))
        
        isValidWord = self.game.take_word_from_board(word, player_id)
        return json.dumps({'is_valid': isValidWord, 'game_state': self.game.get_dict_repr(include_tile_pos = False)})


    @route('/newGame')
    def new_game(self):
        self.game.reset()
        return json.dumps({'game_state': self.game.get_dict_repr(include_tile_pos = True)})


    @route('/generateBoard')
    def generate_board(self):
        return json.dumps({'game_state': self.game.get_dict_repr(include_tile_pos = True)})
    
    @route('/addPlayer')
    def add_player(self):
        player_name = request.args.get('player_name', None)
        self.game.player_store.add_player(player_name)
        return json.dumps({'game_state': self.game.get_dict_repr(include_tile_pos = False)})

SnatchItApp.register(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
