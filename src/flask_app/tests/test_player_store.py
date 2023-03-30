import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

import unittest
import test_utilities
from player_store import PlayerStore

class PlayerStoreTestCase(unittest.TestCase):
    def setUp(self):
        self.player_store = PlayerStore()

    def tearDown(self):
        self.player_store.reset()

    def test_add_player_success(self):
        self.player_store.add_player(0, 'Wes')
        self.assertEqual(self.player_store.num_players(), 1)
        self.player_store.add_player(1, 'Janice')
        self.assertEqual(self.player_store.num_players(), 2)

    def test_add_player_failure(self):
        self.player_store.add_player(0, 'Wes')
        self.assertEqual(self.player_store.num_players(), 1)
        with self.assertRaises(KeyError):
          self.player_store.add_player(0, 'Wes')

    def test_get_dict_repr(self):
        self.player_store.add_player(0, 'Wes')
        self.player_store.add_player(1, 'Janice')
        hello_word = test_utilities.get_hello_word()
        self.player_store.add_player_word(hello_word, 0)
        world_word = test_utilities.get_world_word()
        self.player_store.add_player_word(world_word, 1)
        dict_repr = self.player_store.get_dict_repr()
        
        dict_repr_true = {
          "players": [
              {
                  0: {
                      "name": "Wes",
                      "points": 5,
                      "words": [
                          {
                              "hello": [
                                  {"id": "h0", "letter": "h"},
                                  {"id": "e0", "letter": "e"},
                                  {"id": "l0", "letter": "l"},
                                  {"id": "l1", "letter": "l"},
                                  {"id": "o0", "letter": "o"},
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
                                  {"id": "w0", "letter": "w"},
                                  {"id": "o1", "letter": "o"},
                                  {"id": "r0", "letter": "r"},
                                  {"id": "l2", "letter": "l"},
                                  {"id": "d0", "letter": "d"},
                              ]
                          }
                      ],
                      "id": 1,
                  },
              }
            ]
        }
        
        self.assertEqual(dict_repr, dict_repr_true)



if __name__ == '__main__':
    unittest.main()