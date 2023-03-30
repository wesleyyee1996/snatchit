from word import Word
from tile import Tile

def get_hello_word():
    hello_word = Word(
        [Tile('h', 0), Tile('e', 0), Tile('l', 0), Tile('l', 1), Tile('o', 0)])
    return hello_word

def get_world_word():
    world_word = Word(
        [Tile('w', 0), Tile('o', 1), Tile('r', 0), Tile('l', 2), Tile('d', 0)])
    return world_word