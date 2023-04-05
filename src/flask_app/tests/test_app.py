import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

import unittest
import json
from app import SnatchItApp, app

class SnatchItAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        self.app = app.test_client()

    def test_generate_board(self):
        response = self.app.get('/api/generateBoard')
        self.assertEqual(response.status_code, 200)
        data = json.loads(self.app.get('/api/generateBoard').data)
        self.assertEqual(len(data['game_state']['tiles_on_board']), 100)

    def test_new_game(self):
        response = self.app.get('/api/generateBoard')
        self.assertEqual(response.status_code, 200)
        old_game_state = json.loads(response.data)['game_state']

        new_game_response = self.app.get('/api/newGame')
        self.assertEqual(new_game_response.status_code, 200)

        new_game_response = self.app.get('/api/addPlayer?player_id=0&player_name=Bill')
        self.assertEqual(new_game_response.status_code, 200)

        new_game_state = json.loads(new_game_response.data)['game_state']
        self.assertNotEqual(old_game_state['tiles_on_board'], new_game_state['tiles_on_board'])
        self.assertNotEqual(old_game_state['player_store'], new_game_state['player_store'])

    def test_flip_tile(self):
        flip_tile_resp = self.app.get('/api/tile?tile_id=h0')
        self.assertEqual(flip_tile_resp.status_code, 200)
        data = json.loads(flip_tile_resp.data)
        self.assertTrue(data['game_state']['tiles_on_board']['h0']['is_flipped'])

    def test_submit_word(self):
        response = self.app.get('/api/word?word=hello&player_id=1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertFalse(data['is_valid'])

        self.app.get('/api/addPlayer?player_id=0&player_name=Wes')
        self.app.get('/api/addPlayer?player_id=1&player_name=Bar')
        
        self.app.get('/api/tile?tile_id=h0')
        self.app.get('/api/tile?tile_id=e0')
        self.app.get('/api/tile?tile_id=l0')
        self.app.get('/api/tile?tile_id=l1')
        self.app.get('/api/tile?tile_id=o0')

        response = self.app.get('/api/word?word=hello&player_id=0')
        self.assertTrue(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['is_valid'])
        self.assertIn('hello', data['game_state']['player_store']['players'][0]['0']['words'][0].keys())
        self.assertNotIn('h0', data['game_state']['tiles_on_board'].keys())
        self.assertNotIn('e0', data['game_state']['tiles_on_board'].keys())
        self.assertNotIn('l0', data['game_state']['tiles_on_board'].keys())
        self.assertNotIn('l1', data['game_state']['tiles_on_board'].keys())
        self.assertNotIn('o0', data['game_state']['tiles_on_board'].keys())

    def test_add_player(self):
        response = self.app.get('/api/addPlayer?player_id=0&player_name=Bob')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/api/addPlayer?player_id=0&player_name=Bob')
        data = json.loads(response.data)
        self.assertEqual(data['status'], 500)
        response = self.app.get('/api/addPlayer?player_name=Wes&player_id=1')
        data = json.loads(response.data)
        self.assertEqual(data['game_state']['player_store']['players'])


if __name__ == '__main__':
    unittest.main()