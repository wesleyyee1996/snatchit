import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)

sys.path.append(parent_directory)

from tile import Tile
from word import Word
from player import Player
import test_utilities
import unittest

class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Player('Wes')
        self.hello_word = test_utilities.get_hello_word()
        self.world_word = test_utilities.get_world_word()

    def tearDown(self):
        self.player.reset()
        self.hello_word.reset()
        self.world_word.reset()

    def test_add_word(self):
        self.assertEqual(len(self.player.words), 0)
        self.player.add_word(self.hello_word)

        self.assertEqual(len(self.player.words), 1)
        self.assertEqual(str(self.player.words[0]), 'hello')

        self.player.add_word(self.world_word)
        self.assertEqual(len(self.player.words), 2)

    def test_remove_word(self):
        self.player.add_word(self.hello_word)

        self.assertEqual(len(self.player.words), 1)
        self.assertEqual(str(self.player.words[0]), 'hello')
        self.player.remove_word(self.hello_word)
        self.assertEqual(len(self.player.words), 0)

    def test_get_json(self):
        self.assertEqual(len(self.player.words), 0)
        self.player.add_word(self.hello_word)
        dict_repr = self.player.get_dict_repr()

        dict_repr_true = {
            "name": "Wes",
            "points": 5,
            "words": {
                "hello": {
                    "h0": {"id": "h0", "letter": "h", "is_flipped": False},
                    "e0": {"id": "e0", "letter": "e", "is_flipped": False},
                    "l0": {"id": "l0", "letter": "l", "is_flipped": False},
                    "l1": {"id": "l1", "letter": "l", "is_flipped": False},
                    "o0": {"id": "o0", "letter": "o", "is_flipped": False},
                }
            },
        }

        self.assertEqual(dict_repr, dict_repr_true)

        self.player.add_word(self.world_word)
        dict_repr = self.player.get_dict_repr()

        dict_repr_true = {
            "name": "Wes",
            "points": 10,
            "words": {
                "hello": {
                    "h0": {"id": "h0", "letter": "h", "is_flipped": False},
                    "e0": {"id": "e0", "letter": "e", "is_flipped": False},
                    "l0": {"id": "l0", "letter": "l", "is_flipped": False},
                    "l1": {"id": "l1", "letter": "l", "is_flipped": False},
                    "o0": {"id": "o0", "letter": "o", "is_flipped": False},
                },
                "world": {
                    "w0": {"id": "w0", "letter": "w", "is_flipped": False},
                    "o1": {"id": "o1", "letter": "o", "is_flipped": False},
                    "r0": {"id": "r0", "letter": "r", "is_flipped": False},
                    "l2": {"id": "l2", "letter": "l", "is_flipped": False},
                    "d0": {"id": "d0", "letter": "d", "is_flipped": False},
                },
            },
        }
        self.assertEqual(dict_repr, dict_repr_true)

    


if __name__ == '__main__':
    unittest.main()
