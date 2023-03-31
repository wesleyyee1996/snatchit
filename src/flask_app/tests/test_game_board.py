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
        self.game.add_player('Wes')
        self.game.add_player('Janice')

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

        with self.assertRaises(KeyError):
            self.game.set_letter_flipped('b8')

    def test_tiles_in_play(self):
        self.assertEqual(self.game.tiles_in_play(), [])
        self.game.set_letter_flipped('h0')
        self.assertEqual(self.game.tiles_in_play()[0].id, 'h0')

    def test_is_valid_word(self):
        self.set_letters_flipped(['h0', 'e0', 'l1', 'l0', 'o2', 'b1'])
        is_valid_word, word_to_give = self.game.is_valid_word('hello')
        self.assertTrue(is_valid_word)
        self.assertEqual(str(word_to_give), 'hello')
        self.assertEqual(self.game.tiles_in_play()[0].id, 'b1')

        is_valid_word, word_to_give = self.game.is_valid_word('world')
        self.assertFalse(is_valid_word)

    def test_take_word_from_board(self):
        self.set_letters_flipped(['h0', 'e0', 'l1', 'l0', 'o2', 'b1'])
        isSuccess = self.game.take_word_from_board('hello', 0)
        self.assertTrue(isSuccess)
        self.assertEqual(str(self.game.player_store.players[0].words[0]), 'hello')
        self.assert_tiles_not_on_board(['h0', 'e0', 'l1', 'l0', 'o2'])

        isSuccess = self.game.take_word_from_board('world', 1)
        self.assertFalse(isSuccess)
        self.assertEqual(len(self.game.player_store.players[0].words), 1)
        self.assertEqual(len(self.game.player_store.players[1].words), 0)

        self.set_letters_flipped(['w0', 'o1', 'r0', 'l2', 'd0'])
        isSuccess = self.game.take_word_from_board('world', 1)
        self.assertTrue(isSuccess)
        self.assertEqual(str(self.game.player_store.players[1].words[0]), 'world')
        self.assert_tiles_not_on_board(['w0', 'o1', 'r0', 'l2', 'd0'])

        self.assertEquals(len(self.game.tiles_on_board), 90)


    def test_get_dict_repr(self):
        self.set_letters_flipped(['h0', 'e0', 'l1', 'l0', 'o2', 'b1'])
        self.game.player_store.add_player_word(test_utilities.get_hello_word(), 0)
        self.game.player_store.add_player_word(test_utilities.get_world_word(), 1)

        dict_repr = self.game.get_dict_repr(include_tile_pos=False)
        dict_repr_true = get_dict_repr_true()

        self.assertEqual(dict_repr, dict_repr_true)


    def set_letters_flipped(self, letters_to_flip):
        for letter in letters_to_flip:
            self.game.set_letter_flipped(letter)

    def assert_tiles_not_on_board(self, tiles):
        for tile in tiles:
            self.assertNotIn(tile, self.game.tiles_on_board)

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

def get_dict_repr_true():
    return {
    "tiles_on_board": {
                "a0": {"id": "a0", "letter": "a", "is_flipped": False},
                "a1": {"id": "a1", "letter": "a", "is_flipped": False},
                "a2": {"id": "a2", "letter": "a", "is_flipped": False},
                "a3": {"id": "a3", "letter": "a", "is_flipped": False},
                "a4": {"id": "a4", "letter": "a", "is_flipped": False},
                "b0": {"id": "b0", "letter": "b", "is_flipped": False},
                "b1": {"id": "b1", "letter": "b", "is_flipped": True},
                "c0": {"id": "c0", "letter": "c", "is_flipped": False},
                "c1": {"id": "c1", "letter": "c", "is_flipped": False},
                "c2": {"id": "c2", "letter": "c", "is_flipped": False},
                "c3": {"id": "c3", "letter": "c", "is_flipped": False},
                "d0": {"id": "d0", "letter": "d", "is_flipped": False},
                "d1": {"id": "d1", "letter": "d", "is_flipped": False},
                "d2": {"id": "d2", "letter": "d", "is_flipped": False},
                "d3": {"id": "d3", "letter": "d", "is_flipped": False},
                "e0": {"id": "e0", "letter": "e", "is_flipped": True},
                "e1": {"id": "e1", "letter": "e", "is_flipped": False},
                "e2": {"id": "e2", "letter": "e", "is_flipped": False},
                "e3": {"id": "e3", "letter": "e", "is_flipped": False},
                "e4": {"id": "e4", "letter": "e", "is_flipped": False},
                "e5": {"id": "e5", "letter": "e", "is_flipped": False},
                "e6": {"id": "e6", "letter": "e", "is_flipped": False},
                "e7": {"id": "e7", "letter": "e", "is_flipped": False},
                "e8": {"id": "e8", "letter": "e", "is_flipped": False},
                "e9": {"id": "e9", "letter": "e", "is_flipped": False},
                "e10": {"id": "e10", "letter": "e", "is_flipped": False},
                "e11": {"id": "e11", "letter": "e", "is_flipped": False},
                "f0": {"id": "f0", "letter": "f", "is_flipped": False},
                "f1": {"id": "f1", "letter": "f", "is_flipped": False},
                "f2": {"id": "f2", "letter": "f", "is_flipped": False},
                "f3": {"id": "f3", "letter": "f", "is_flipped": False},
                "g0": {"id": "g0", "letter": "g", "is_flipped": False},
                "g1": {"id": "g1", "letter": "g", "is_flipped": False},
                "h0": {"id": "h0", "letter": "h", "is_flipped": True},
                "h1": {"id": "h1", "letter": "h", "is_flipped": False},
                "h2": {"id": "h2", "letter": "h", "is_flipped": False},
                "h3": {"id": "h3", "letter": "h", "is_flipped": False},
                "h4": {"id": "h4", "letter": "h", "is_flipped": False},
                "i0": {"id": "i0", "letter": "i", "is_flipped": False},
                "i1": {"id": "i1", "letter": "i", "is_flipped": False},
                "i2": {"id": "i2", "letter": "i", "is_flipped": False},
                "i3": {"id": "i3", "letter": "i", "is_flipped": False},
                "i4": {"id": "i4", "letter": "i", "is_flipped": False},
                "j0": {"id": "j0", "letter": "j", "is_flipped": False},
                "k0": {"id": "k0", "letter": "k", "is_flipped": False},
                "l0": {"id": "l0", "letter": "l", "is_flipped": True},
                "l1": {"id": "l1", "letter": "l", "is_flipped": True},
                "l2": {"id": "l2", "letter": "l", "is_flipped": False},
                "l3": {"id": "l3", "letter": "l", "is_flipped": False},
                "l4": {"id": "l4", "letter": "l", "is_flipped": False},
                "m0": {"id": "m0", "letter": "m", "is_flipped": False},
                "m1": {"id": "m1", "letter": "m", "is_flipped": False},
                "m2": {"id": "m2", "letter": "m", "is_flipped": False},
                "m3": {"id": "m3", "letter": "m", "is_flipped": False},
                "n0": {"id": "n0", "letter": "n", "is_flipped": False},
                "n1": {"id": "n1", "letter": "n", "is_flipped": False},
                "n2": {"id": "n2", "letter": "n", "is_flipped": False},
                "n3": {"id": "n3", "letter": "n", "is_flipped": False},
                "n4": {"id": "n4", "letter": "n", "is_flipped": False},
                "o0": {"id": "o0", "letter": "o", "is_flipped": False},
                "o1": {"id": "o1", "letter": "o", "is_flipped": False},
                "o2": {"id": "o2", "letter": "o", "is_flipped": True},
                "o3": {"id": "o3", "letter": "o", "is_flipped": False},
                "o4": {"id": "o4", "letter": "o", "is_flipped": False},
                "o5": {"id": "o5", "letter": "o", "is_flipped": False},
                "p0": {"id": "p0", "letter": "p", "is_flipped": False},
                "p1": {"id": "p1", "letter": "p", "is_flipped": False},
                "p2": {"id": "p2", "letter": "p", "is_flipped": False},
                "q0": {"id": "q0", "letter": "q", "is_flipped": False},
                "r0": {"id": "r0", "letter": "r", "is_flipped": False},
                "r1": {"id": "r1", "letter": "r", "is_flipped": False},
                "r2": {"id": "r2", "letter": "r", "is_flipped": False},
                "r3": {"id": "r3", "letter": "r", "is_flipped": False},
                "r4": {"id": "r4", "letter": "r", "is_flipped": False},
                "s0": {"id": "s0", "letter": "s", "is_flipped": False},
                "s1": {"id": "s1", "letter": "s", "is_flipped": False},
                "s2": {"id": "s2", "letter": "s", "is_flipped": False},
                "s3": {"id": "s3", "letter": "s", "is_flipped": False},
                "s4": {"id": "s4", "letter": "s", "is_flipped": False},
                "t0": {"id": "t0", "letter": "t", "is_flipped": False},
                "t1": {"id": "t1", "letter": "t", "is_flipped": False},
                "t2": {"id": "t2", "letter": "t", "is_flipped": False},
                "t3": {"id": "t3", "letter": "t", "is_flipped": False},
                "t4": {"id": "t4", "letter": "t", "is_flipped": False},
                "t5": {"id": "t5", "letter": "t", "is_flipped": False},
                "t6": {"id": "t6", "letter": "t", "is_flipped": False},
                "u0": {"id": "u0", "letter": "u", "is_flipped": False},
                "u1": {"id": "u1", "letter": "u", "is_flipped": False},
                "u2": {"id": "u2", "letter": "u", "is_flipped": False},
                "u3": {"id": "u3", "letter": "u", "is_flipped": False},
                "v0": {"id": "v0", "letter": "v", "is_flipped": False},
                "v1": {"id": "v1", "letter": "v", "is_flipped": False},
                "w0": {"id": "w0", "letter": "w", "is_flipped": False},
                "w1": {"id": "w1", "letter": "w", "is_flipped": False},
                "w2": {"id": "w2", "letter": "w", "is_flipped": False},
                "x0": {"id": "x0", "letter": "x", "is_flipped": False},
                "y0": {"id": "y0", "letter": "y", "is_flipped": False},
                "y1": {"id": "y1", "letter": "y", "is_flipped": False},
                "y2": {"id": "y2", "letter": "y", "is_flipped": False},
                "z0": {"id": "z0", "letter": "z", "is_flipped": False},
            },
            "player_store": {
                "players": [
                    {
                        0: {
                            "name": "Wes",
                            "points": 5,
                            "words": [
                                {
                                    "hello": [
                                        {"id": "h0", "letter": "h", "is_flipped": False},
                                        {"id": "e0", "letter": "e", "is_flipped": False},
                                        {"id": "l0", "letter": "l", "is_flipped": False},
                                        {"id": "l1", "letter": "l", "is_flipped": False},
                                        {"id": "o0", "letter": "o", "is_flipped": False},
                                    ]
                                }
                            ],
                            "id": 0,
                        },
                        1: {
                            "name": "Janice",
                            "points": 5,
                            "words": [
                                {
                                    "world": [
                                        {"id": "w0", "letter": "w", "is_flipped": False},
                                        {"id": "o1", "letter": "o", "is_flipped": False},
                                        {"id": "r0", "letter": "r", "is_flipped": False},
                                        {"id": "l2", "letter": "l", "is_flipped": False},
                                        {"id": "d0", "letter": "d", "is_flipped": False},
                                    ]
                                }
                            ],
                            "id": 1,
                        },
                    }
                ]
            },
        }


if __name__ == '__main__':
    unittest.main()