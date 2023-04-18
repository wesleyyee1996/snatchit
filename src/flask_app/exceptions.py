

class WordIsTooShortException(Exception):
    def __init__(self, word, min_len):
        self.message = f"The word '{word}' is too short. It must be at least {min_len} letter long!"
        super().__init__(self.message)


class WordDoesNotExistInDictionaryException(Exception):
    def __init__(self, word):
        self.message = f"The word '{word}' doesn't exist in the dictionary!"
        super().__init__(self.message)


class CannotMakeWordFromGameTilesException(Exception):
    def __init__(self, word):
        self.message = f"The word '{word}' can't be made from the tiles on the board!"
        super().__init__(self.message)
