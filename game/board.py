from game.cell import Cell


class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]
    
    def validate_word_inside_board(self, word, location, orientation):
        row, col = location

    def validate_word_inside_board(self, word, location: tuple, orientation):
        horizontal_position = location[0]
        vertical_position = location[1]
        len_word = len(word)
        orientation = orientation.upper()
      
        if orientation == "V":
            if vertical_position + len_word > 15:
                return False
            elif horizontal_position + len_word > 1:
                return True 
        elif orientation == "H":
            if horizontal_position + len_word > 15:
                return False
            elif vertical_position + len_word > 1:
                return True 
    
    