import unittest
from game.player import Player
from game.models import Tile, BagTiles
from game.scrabble import ScrabbleGame


class TestPlayer(unittest.TestCase): #Objetivo revisar que usuario comience con cero fichas
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )
        self.assertEqual(player_1.points_player, 0)
    
        """_summary_
        """     
    def test_make_play_user_has_letter(self): #Objetivo camino palabra ingresada correctamente
        player_1 = Player()
        player_1.tiles = ["h", "o", "l", "a", "b", "j"] #Fichas jugador 
        word = player_1.make_play("hola")  #Llamado a funcion con word = hola
        self.assertEquals(word,  
    "hola"        
        )
        self.assertEqual(len(player_1.tiles), 2) #Se restan 4 fichas "hola" a 6 fichas 
    
    def test_make_play_user_has_not_letter(self): #Camino no valido 
        player_1 = Player()
        player_1.tiles = ["h", "o", "l", "a", "b", "j"] 
        word = player_1.make_play("hacer")  #Cuando alguna letra no es en sus fichas retorna None
        self.assertEqual(word, None) 
        self.assertEqual(len(player_1.tiles), 6) #Las fichas se mantienen iguales
        
    def test_put_tiles_to_bagtiles(self):
        player_1 = Player()
        player_1.tiles = ["h", "o", "l", "a", "b", "j"] 
        word = player_1.put_tiles_to_bagtiles(["h", "o", "b"])
        self.assertEqual(player_1.tiles, ["l", "a" , "j"] )
        self.assertEqual(len(player_1.tiles), 3)
       
    def test_take_tiles_from_bagtiles(self):
        player_1 = Player()
        player_1.tiles = ["h", "o", "l", "a", "b", "j"] 
        tiles = player_1.take_tiles_from_bagtiles(["m", "n", "c"])
        self.assertEqual(player_1.tiles, ["h", "o", "l", "a", "b", "j", "m", "n", "c"] )
        self.assertEqual(len(player_1.tiles), 9)
    
       
    def test_point_from_calculation(self):
        scrabble_game = ScrabbleGame(players_count = 3)
        bag_tiles = BagTiles()
        scrabble_game.current_player = Player()
        scrabble_game.current_player.tiles = [Tile("C", 1), Tile("A", 1), Tile("S", 2), Tile("A", 1)]
        scrabble_game.calculate_word_value("CASA", (7,7), "V")
        self.assertEqual(scrabble_game.current_player.points, 5,)
    


if __name__ == '__main__':
    unittest.main()