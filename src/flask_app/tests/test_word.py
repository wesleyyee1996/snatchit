import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

import unittest
from word import Word
from tile import Tile
import json

class WordTestCase(unittest.TestCase):
    def setUp(self):
        self.word = Word()

    def tearDown(self):
        self.word.reset()

    def test_get_dict_repr(self):
        self.word.add_tile(Tile('h', 0))
        self.word.add_tile(Tile('e', 0))
        self.word.add_tile(Tile('l', 0))
        self.word.add_tile(Tile('l', 1))
        self.word.add_tile(Tile('o', 0))
        dict_repr = self.word.get_dict_repr()
        self.assertIn('hello', dict_repr)
        self.assertEqual(len(dict_repr['hello']), 5)
        self.assertEqual(dict_repr['hello'][0]['id'], 'h0')
        self.assertEqual(dict_repr['hello'][1]['id'], 'e0')
        self.assertEqual(dict_repr['hello'][2]['id'], 'l0')
        self.assertEqual(dict_repr['hello'][3]['id'], 'l1')
        self.assertEqual(dict_repr['hello'][4]['id'], 'o0')


if __name__ == '__main__':
    unittest.main()