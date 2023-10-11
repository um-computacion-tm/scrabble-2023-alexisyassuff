from game.models import Tile
class Cell:
    def __init__(self, letter=None, multiplier=1, multiplier_type=None):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
    def add_letter(self, letter:Tile):
        self.letter = letter
    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
        
    def __repr__(self):
        if self.tile:
            return repr(self.tile)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return 