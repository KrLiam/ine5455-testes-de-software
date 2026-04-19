import unittest

from conteudo.puzzle_game import PuzzleGame, InvalidPositionException
from tests.shufflers_for_testing_puzzles import *

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


class TesteMutantes(unittest.TestCase):
    def test__line_0(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        with self.assertRaises(InvalidPositionException):
            game.get_tile(0, 1)

    def test__column_0(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        with self.assertRaises(InvalidPositionException):
            game.get_tile(1, 0)

    # Mata mutante 34
    def test_ramo_0_1_2_3_4(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        # Exercise SUT
        sucesso = game.move_tile(6)

        # Result Verification
        self.assertEqual(sucesso, True)
    
    # Mata mutante 3 e 35
    def test_ramo_0_1_2_5(self):
        # Inline Fixture Setup
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
        game.dic_positions_of_tiles[6] = (4, 3)

        # Exercise SUT
        sucesso = game.move_tile(6)

        # Result Verification
        self.assertEqual(sucesso, False)

    def test_move_tile_from_a_position_to_the_empty_position_returns_false(self):
        game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
        result = game.move_tile_from_a_position_to_the_empty_position(-1, 0)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

