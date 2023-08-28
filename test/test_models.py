import unittest
from game.models import (
    BagTiles,
    Tile,
)
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tileaeeilnorstu(self):
        tile = Tile('A' and "E" and "I" and "L" and "N" and "O" and "R" and"S" and "T" and "U", 1)
        self.assertEqual(tile.letter, 'A' and "E" and "I" and "L" and "N" and "O" and "R" and"S" and "T" and "U")
        self.assertEqual(tile.value, 1)
    def test_tiledg(self):
        tile = Tile("D" and "G", 2)
        self.assertEqual(tile.letter, "D" and "G")
        self.assertEqual(tile.value, 2)
    def test_tilebcmp(self):
        tile = Tile("B" and "C" and "M" and "P", 3)
        self.assertEqual(tile.letter,"B" and "C" and "M" and "P")
        self.assertEqual(tile.value, 3)
    def test_tilefhvy(self):
        tile = Tile("F" and "H" and "V" and "Y", 4)
        self.assertEqual(tile.letter, "F" and "H" and "V" and "Y")
        self.assertEqual(tile.value, 4)
    def test_tile_jllñrx(self):
        tile = Tile("J" and "LL" and "Ñ" and "R" and "X" , 8)
        self.assertEqual(tile.letter, "J" and "LL" and "Ñ" and "R" and "X")
        self.assertEqual(tile.value, 8)
    def test_tile_z(self):
        tile = Tile("Z", 10)
        self.assertEqual(tile.letter, "Z")
        self.assertEqual(tile.value, 10)
    def test_tile_comodin(self):
        tile = Tile("Comodin", 0)
        self.assertEqual(tile.letter, 'Comodin')
        self.assertEqual(tile.value, 0)
        
class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            100,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )


    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            98,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            100,
        )


if __name__ == '__main__':
    unittest.main()