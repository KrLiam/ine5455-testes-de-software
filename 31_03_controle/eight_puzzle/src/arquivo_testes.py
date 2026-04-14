import unittest

from shufflers_for_testing_puzzles import *
from puzzle_game import PuzzleGame


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

