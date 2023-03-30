import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

import unittest
import json
from app import SnatchItApp

class MyFlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = SnatchItApp().app.test_client()

    def tearDown(self):
        self.app = SnatchItApp().app.test_client()

    def test_generate_board(self):
        response = self.app.get('/api/generateBoard')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.text)), 100)

    def test_new_game(self):
        response = self.app.get('/api/generateBoard')
        old_board = json.loads(response.text)
        # new_game_response = self.app.get('/api/newgame')
        # new_board = json.loads(new_game_response.text)
        # self.assertNotEqual(old_board, new_board)


    def test_submit_word(self):
        response = self.app.get('/api/word?word=hello&player_id=1')
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b'Welcome to my app', response.data)


if __name__ == '__main__':
    unittest.main()