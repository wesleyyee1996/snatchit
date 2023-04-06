from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_classful import FlaskView, route
from game_board import GameBoard
import json

app = Flask(__name__)
CORS(app)
game = GameBoard()

class SnatchItApp(FlaskView):
    route_base = '/'
    route_prefix = '/api/'

    def __init__(self):
        print('RESET')
        # self.game = GameBoard()

    @route('/tile')
    def tile(self):
        tile_id = request.args.get('tile_id', None)
        game.set_letter_flipped(tile_id)
        return json.dumps({'game_state': game.get_dict_repr(include_tile_pos = False)})
    
    @route('/word')
    def word(self):
        word = request.args.get('word', None)
        player_id = int(request.args.get('player_id', None))
        
        isValidWord = game.submit_word(word, player_id)
        return json.dumps({'is_valid': isValidWord, 'game_state': game.get_dict_repr(include_tile_pos = False)})

    @route('/newGame')
    def new_game(self):
        game.reset()
        return json.dumps({'game_state': game.get_dict_repr(include_tile_pos = True)})

    @route('/generateBoard')
    def generate_board(self):
        return json.dumps({'game_state': game.get_dict_repr(include_tile_pos = True)})
    
    @route('/addPlayer')
    def add_player(self):
        player_id = int(request.args.get('player_id', None))
        player_name = request.args.get('player_name', None)
        status = 200
        try:
            game.add_player(player_id, player_name)
        except KeyError as e:
            status = 500
        return json.dumps({'status': status, 'game_state': game.get_dict_repr(include_tile_pos = False)})

SnatchItApp.register(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
