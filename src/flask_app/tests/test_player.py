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

    def test_get_json(self):
        self.assertEqual(len(self.player.words), 0)
        self.player.add_word(self.hello_word)
        dict_repr = self.player.get_dict_repr()

        dict_repr_true = {
            'name': 'Wes',
            'points': 5,
            'words': [
                {'hello':
                 [
                    {'id': 'h0', 'letter': 'h'},
                     {'id': 'e0', 'letter': 'e'},
                     {'id': 'l0', 'letter': 'l'},
                     {'id': 'l1', 'letter': 'l'},
                     {'id': 'o0', 'letter': 'o'}
                 ]
                 }
            ]
        }

        self.assertEqual(dict_repr, dict_repr_true)

        self.player.add_word(self.world_word)
        dict_repr = self.player.get_dict_repr()

        dict_repr_true = {
            "name": "Wes",
            "points": 10,
            "words": [
                {
                    "hello": [
                        {"id": "h0", "letter": "h"},
                        {"id": "e0", "letter": "e"},
                        {"id": "l0", "letter": "l"},
                        {"id": "l1", "letter": "l"},
                        {"id": "o0", "letter": "o"},
                    ]
                },
                {
                    "world": [
                        {"id": "w0", "letter": "w"},
                        {"id": "o1", "letter": "o"},
                        {"id": "r0", "letter": "r"},
                        {"id": "l2", "letter": "l"},
                        {"id": "d0", "letter": "d"},
                    ]
                },
            ],
        }
        self.assertEqual(dict_repr, dict_repr_true)

    


if __name__ == '__main__':
    unittest.main()
