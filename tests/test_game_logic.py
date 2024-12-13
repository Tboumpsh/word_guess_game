# test_game_logic.py

import unittest
from game.game_logic import check_guess, choose_word

class TestGameLogic(unittest.TestCase):
    def test_check_guess_correct(self):
        self.assertTrue(check_guess("Python", "python"))

    def test_check_guess_incorrect(self):
        self.assertFalse(check_guess("Python", "java"))

    def test_choose_word(self):
        words = ["Python", "Java", "C++"]
        self.assertIn(choose_word(words), words)

if __name__ == "__main__":
    unittest.main()
