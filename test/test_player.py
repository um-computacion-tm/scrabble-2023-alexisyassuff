import unittest
from game.player import Player


class TestPlayer(unittest.TestCase): #Objetivo revisar que usuario comience con cero fichas
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )
    
     
    def test_hacer_jugada(self): #Objetivo 
        player_1 = Player()
        player_1.tiles = ["h", "o", "l", "a"]
        palabra = player_1.hacer_jugada("hola") 
        self.assertEquals(palabra, 
    "hola"        
        )
        

if __name__ == '__main__':
    unittest.main()