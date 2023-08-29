import unittest
from game.player import Player


class TestPlayer(unittest.TestCase): #Objetivo revisar que usuario comience con cero fichas
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )
    
     
    def test_make_play_valid_word(self): #Objetivo camino palabra ingresada correctamente
        player_1 = Player()
        player_1.tiles = ["h", "o", "l", "a", "b", "j"] #Fichas jugador 
        word = player_1.make_play("hola")  #Llamado a funcion con word = hola
        self.assertEquals(word,  
    "hola"        
        )
        self.assertEqual(len(player_1.tiles), 2) #Se restan 4 fichas "hola" a 6 fichas 
    
    def test_make_play_not_valid_word(self): #Camino no valido 
        player_1 = Player()
        player_1.tiles = ["h", "o", "l", "a", "b", "j"] 
        word = player_1.make_play("hacer") #Cuando alguna letra no es en sus fichas retorna None
        self.assertEqual(word, None) 
        self.assertEqual(len(player_1.tiles), 6) #Las fichas se mantienen iguales

if __name__ == '__main__':
    unittest.main()