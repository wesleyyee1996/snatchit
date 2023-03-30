from flask import Flask, jsonify, request
from flask_cors import CORS
from game_board import GameBoard
import json


class SnatchItApp:
    app = Flask(__name__)
    CORS(app)

    def __init__(self):
        self.configure_routes()
        self.game = GameBoard()

    def configure_routes(self):

        @self.app.route('/api/word', methods=['GET'])
        def submit_word():
            word = request.args.get('word', None)
            player_id = int(request.args.get('player_id', None))
            
            isValidWord, tilesMoved = self.game.take_word_from_board(word, player_id)
            if isValidWord:
                return json.dumps({'is_valid': True, 'tiles_moved': tilesMoved})
            return json.dumps({'is_valid':False})


        @self.app.route('/api/tile', methods=['POST'])
        def letter_flipped():
            self.game.set_letter_flipped(request.args.get('tile_id', None))
            return self.game.get_board_state_json()


        @self.app.route('/api/newgame')
        def new_game():
            self.game.reset()
            return jsonify(success=True)


        @self.app.route('/api/generateBoard')
        def generate_board():
            return self.game.get_board_state_json()


if __name__ == '__main__':
    snatch_it_app = SnatchItApp()
    snatch_it_app.app.run(host="0.0.0.0", port=8000, debug=True)
