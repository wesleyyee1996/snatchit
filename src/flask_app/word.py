

class Word:
    def __init__(self, tiles = []):
        self.tiles = tiles

    def __repr__(self):
        word = ''
        for t in self.tiles:
            word += t.letter
        return word
    
    def __len__(self):
        return len(self.tiles)
    
    def add_tile(self, tile):
        """
        Input:
          tile: a Tile object
        """
        self.tiles.append(tile)

    def tile_ids(self):
        return [t.id for t in self.tiles]
