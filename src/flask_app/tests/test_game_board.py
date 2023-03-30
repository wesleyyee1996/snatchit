import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

import unittest
from game_board import GameBoard
import test_utilities

class GameBoardTestCase(unittest.TestCase):
    def setUp(self):
        self.game = GameBoard()
        self.game.add_player(0, 'Wes')
        self.game.add_player(1, 'Janice')

    def tearDown(self):
        self.game.reset()

    def test_generate_board(self):
        tiles_on_board = self.game.tiles_on_board
        self.assertEqual(len(tiles_on_board), 100)

    def test_reset_board(self):
        tiles_on_board_old = self.game.tiles_on_board
        self.game.reset()
        tiles_on_board_new = self.game.tiles_on_board
        self.assertNotEqual(tiles_on_board_old, tiles_on_board_new)

    def test_set_letter_flipped(self):
        self.game.set_letter_flipped('a0')
        self.assertTrue(self.game.tiles_on_board['a0'].is_flipped)

    def test_tiles_in_play(self):
        self.assertEqual(self.game.tiles_in_play(), [])
        self.game.set_letter_flipped('h0')
        self.assertEqual(self.game.tiles_in_play()[0].id, 'h0')

    def test_is_valid_word(self):
        self.game.set_letter_flipped('h0')
        self.game.set_letter_flipped('e0')
        self.game.set_letter_flipped('l1')
        self.game.set_letter_flipped('l0')
        self.game.set_letter_flipped('o2')
        self.game.set_letter_flipped('b1')
        is_valid_word, word_to_give = self.game.is_valid_word('hello')
        self.assertTrue(is_valid_word)
        self.assertEqual(str(word_to_give), 'hello')
        self.assertEqual(self.game.tiles_in_play()[0].id, 'b1')

        is_valid_word, word_to_give = self.game.is_valid_word('world')
        self.assertFalse(is_valid_word)
        self.assertIsNone(word_to_give)

    def test_take_word_from_board(self):
        self.game.set_letter_flipped('h0')
        self.game.set_letter_flipped('e0')
        self.game.set_letter_flipped('l1')
        self.game.set_letter_flipped('l0')
        self.game.set_letter_flipped('o2')
        self.game.set_letter_flipped('b1')
        self.game.take_word_from_board('hello', 0)

    def test_get_dict_repr(self):
        self.game.set_letter_flipped('h0')
        self.game.set_letter_flipped('e0')
        self.game.set_letter_flipped('l1')
        self.game.set_letter_flipped('l0')
        self.game.set_letter_flipped('o2')
        self.game.set_letter_flipped('b1')
        self.game.player_store.add_player_word(test_utilities.get_hello_word(), 0)
        self.game.player_store.add_player_word(test_utilities.get_world_word(), 1)

        dict_repr = self.game.get_dict_repr()
        print(dict_repr)


    # def test_new_game(self):
        # response = self.app.get('/api/generateBoard')
        # old_board = json.loads(response.text)
        # new_game_response = self.app.get('/api/newgame')
        # new_board = json.loads(new_game_response.text)
        # self.assertNotEqual(old_board, new_board)


    # def test_submit_word(self):
        # response = self.app.get('/api/word?word=hello&player_id=1')
        # self.assertEqual(response.status_code, 200)
        # self.assertIn(b'Welcome to my app', response.data)


if __name__ == '__main__':
    unittest.main()