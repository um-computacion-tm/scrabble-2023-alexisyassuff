from game.board import Board
from game.player import Player
from game.models import BagTiles
from game.dictionary import validate_word


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())
        self.current_player = self.players[0] # Inicializa el jugador actual en None al principio

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            turn = self.players.index(self.current_player)
            if turn == (len(self.players) - 1):
                self.current_player = self.players[0]
            else:
                self.current_player = self.players[turn + 1]
                
    #     1- Validar que usuario tiene esas letras
    #     2- Validar que la palabra entra en el tablero
    def validate_word(self, word, location, orientation):
        self.verify_tiles_in_hand(word)
        self.validate_word_inside_board(word, location, orientation)
        self.validate_word(word)
        ##Atrapar 

    
    # def get_words():
    #     '''
    #     Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
    #     Preguntar al usuario, por cada una de esas palabras, las que considera reales
    #     '''
    
    # def put_words():
    #     def make_play(self, word):

    #     '''
    #     Modifica el estado del tablero con las palabras consideradas como correctas
    #     ''    