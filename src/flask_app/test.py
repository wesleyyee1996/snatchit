from game_board import GameBoard, Tile

gameboard = GameBoard()

gameboard.generate_game_board()
gameboard.generate_tile_positions()

print(gameboard.tile_positions)
