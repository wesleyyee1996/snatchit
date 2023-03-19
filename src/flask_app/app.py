from flask import Flask, jsonify, request
from flask_cors import CORS
from game_board import GameBoard
import json

app = Flask(__name__)
CORS(app)

game = GameBoard()


@app.route('/api/word', methods=['GET'])
def submit_word():
    word = request.args.get('word', None)
    player_id = int(request.args.get('player_id', None))
    
    isValidWord, tilesMoved = game.take_word_from_board(word, player_id)
    print('test', tilesMoved)
    if isValidWord:
        return json.dumps({'is_valid': True, 'tiles_moved': tilesMoved})
    return json.dumps({'is_valid':False})


@app.route('/api/tile', methods=['POST'])
def letter_flipped():
    game.set_letter_flipped(request.args.get('tile_id', None))
    return game.get_board_state_json()


@app.route('/api/newgame')
def new_game():
    global game
    game = GameBoard()
    return jsonify(success=True)


@app.route('/api/generateBoard')
def generate_board():
    return game.get_board_state_json()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
