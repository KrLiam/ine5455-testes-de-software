import unittest

from shufflers_for_testing_puzzles import *
from puzzle_game import PuzzleGame
from invalid_position_exception import InvalidPositionException

class TesteComandos(unittest.TestCase):
    def test_comando_0_1_2_3_4(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        # Exercise SUT
        sucesso = game.move_tile(5)

        # Result Verification
        self.assertEqual(sucesso, True)

    def test_comando_0_1_2_5(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
        game.dic_positions_of_tiles[3] = (1, 4)

        # Exercise SUT
        sucesso = game.move_tile(3)

        # Result Verification
        self.assertEqual(sucesso, False)


class TesteRamos(unittest.TestCase):
    def test_ramo_0_1_2_3_4(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        # Exercise SUT
        sucesso = game.move_tile(6)

        # Result Verification
        self.assertEqual(sucesso, True)
        
    def test_ramo_0_1_2_5(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
        game.dic_positions_of_tiles[6] = (4, 3)

        # Exercise SUT
        sucesso = game.move_tile(6)

        # Result Verification
        self.assertEqual(sucesso, False)

    def test_ramo_0_1_2_3_5(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        # Exercise SUT
        sucesso = game.move_tile(8)
        
        # Result Verification
        self.assertEqual(sucesso, False)


class TesteAllCUsesSomePUses(unittest.TestCase):
    def test__c_uses_some_p_uses__line__0_1_4(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        # Exercise SUT
        tile = game.get_tile(2, 2)

        # Result Verification
        self.assertEqual(tile, 5)

    def test__c_uses_some_p_uses__column__0_1_4(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        # Exercise SUT
        tile = game.get_tile(3, 2)

        # Result Verification
        self.assertEqual(tile, 8)

class TesteAllPUses(unittest.TestCase):
    def test__all_p_uses__line__0_1_3(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        # Exercise SUT
        tile = game.get_tile(2, 3)

        # Result Verification
        self.assertEqual(tile, ' ')

    def test__all_p_uses__line__0_1_4(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        # Exercise SUT
        tile = game.get_tile(1, 1)

        # Result Verification
        self.assertEqual(tile, 1)

    def test__all_p_uses__line__0_2(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        # Exercise SUT
        with self.assertRaises(InvalidPositionException):
            game.get_tile(4, 1)


    def test__all_p_uses__column__0_1_3(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        # Exercise SUT
        tile = game.get_tile(2, 3)

        # Result Verification
        self.assertEqual(tile, ' ')

    def test__all_p_uses__column__0_1_4(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        # Exercise SUT
        tile = game.get_tile(3, 3)

        # Result Verification
        self.assertEqual(tile, 6)

    def test__all_p_uses__column__0_2(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        # Exercise SUT
        with self.assertRaises(InvalidPositionException):
            game.get_tile(1, 4)


if __name__ == "__main__":
    unittest.main()

