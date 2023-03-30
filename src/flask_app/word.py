

class Word:
    def __init__(self, tiles = []):
        self.tiles = tiles

    def __repr__(self):
        self.word = ''
        for t in self.tiles:
            self.word += t.letter
        return self.word
    
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
    
    def get_dict_repr(self):
        return {
            self.__repr__() : [x.get_dict_repr() for x in self.tiles]
        }
    
    def reset(self):
        self.tiles = []
