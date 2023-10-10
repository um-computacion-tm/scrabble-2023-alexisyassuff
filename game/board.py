from game.cell import Cell


class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]
        self.is_empty = True
        
    def validate_word_inside_board(self, word, location: tuple , orientation):
        #Define cual indice de tupla es fila y columna   [f,c]
        horizontal_position = location[0]
        col = location[1]
        len_word = len(word)
        orientation = orientation.upper()
      
        if orientation == "V":
            if  col + len_word > 15:
                return False
            elif horizontal_position + len_word > 1:
                return True 
        elif orientation == "H":
            if horizontal_position + len_word > 15:
                return False
            elif    col + len_word > 1:
                return True 
        
    def validate_word_out_of_board(self, word, location, orientation):
        return not self.validate_word_inside_board(word, location, orientation)
    
    def is_empty(self):
        if self.grid[7][7].letter == None:
            return True  
        else:
            return False
            
    def validate_word_place_board(self, word, location: tuple, orientation):
        len_word = len(word)
        row = location[0]
        col = location[1]
        if orientation == "H":
            return len_word +  col <= 14
        if orientation == "H":
            return len_word +  col > 14
        if orientation == "V":
           return len_word + row <= 14
        if orientation == "V":
           return len_word + row > 14
       
    def show_board(board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )