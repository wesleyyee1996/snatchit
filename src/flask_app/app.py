import json
import uuid
import logging
from game_board import GameBoard
from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = 'my_secret_key'
app.logger.setLevel(logging.DEBUG)
game = GameBoard()

socketio = SocketIO(app, cors_allowed_origins='*')


logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
FORMAT = "[%(lineno)s - %(funcName)20s()] %(message)s"
logging.basicConfig(level=logging.NOTSET, format=FORMAT)


@socketio.on('tile')
def tile(data):
    app.logger.debug('data', data)
    tile_id = data['tile_id']
    game.set_letter_flipped(tile_id)

    emit('update_game', {
         'game_state': game.get_dict_repr(include_tile_pos=False)}, broadcast=True)


@socketio.on('word')
def word(data):
    app.logger.debug('data', data)
    word = data['word']
    player_id = data['player_id']

    isValidWord = game.submit_word(word, player_id)
    emit('update_game', {'is_valid_word': isValidWord,
         'game_state': game.get_dict_repr(include_tile_pos=False)}, broadcast=True)


@socketio.on('new_game')
def new_game():
    game.reset()
    emit('update_game', {
         'game_state': game.get_dict_repr(include_tile_pos=True)}, broadcast=True)


@socketio.on('generate_board')
def generate_board():
    emit('generate_board', {
         'game_state': game.get_dict_repr(include_tile_pos=True)}, broadcast=True)


@socketio.on('add_player')
def add_player(data):
    app.logger.debug('data', data)
    player_id = data['player_id']
    player_name = data['player_name']
    status = 200
    try:
        game.add_player(player_id, player_name)
    except KeyError as e:
        status = 500
    emit('update_game', {
         'game_state': game.get_dict_repr(include_tile_pos=False)}, broadcast=True)


# define your SocketIO event handlers here
@socketio.on('connect')
def handle_connect():
    app.logger.info('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=8000, debug=False)
