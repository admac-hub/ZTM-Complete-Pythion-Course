import unittest
import test_game


class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = test_game.run_guess(guess,answer)
        self.assertTrue(result)

if __name__ =='__main__':
    unittest.main()