from game.cell import Cell


class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]
        self.initialize_multipliers()  # Llama a la función para inicializar los multiplicadores

    def initialize_multipliers(self):
        double_letter_cells = [(4, 1), (12, 1), (1, 4), (8, 4), (15, 4), (3, 7), (7, 7), (9, 7), (13, 7), (4, 10), (12, 10), (0, 12), (7, 12), (14, 12), (3, 15), (11, 15)]
        triple_letter_cells = [(6, 2), (10, 2), (2, 6), (6, 6), (10, 6), (14, 6), (1, 8), (5, 8), (9, 8), (13, 8), (2, 10), (6, 10), (10, 10), (14, 10), (6, 14), (10, 14)]
        double_word_cells = [(1, 1), (8, 1), (15, 1), (2, 2), (14, 2), (3, 3), (13, 3), (4, 4), (12, 4), (7, 7), (11, 7), (4, 12), (12, 12), (1, 15), (8, 15), (15, 15)]
        triple_word_cells = [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)]

      
        
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
    
    def  board_is_empty(self):
        # import ipdb; ipdb.set_trace()
        if self.grid[7][7].letter == None:
            print("a", self.grid[7][7].letter )
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
    
    def add_multiplier(self, row, col, multiplier, multiplier_type):
        pass
        # for i in self.grid
       
    def show_board(board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )

### Added