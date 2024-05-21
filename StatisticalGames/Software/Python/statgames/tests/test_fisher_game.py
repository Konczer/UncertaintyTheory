# tests/test_fisher_game.py
import unittest
from statgames.fisher_game import F

class TestModule(unittest.TestCase):
    def test_F(self):
        self.assertEqual(F(2), 4)
        self.assertEqual(F(0), 0)
        self.assertEqual(F(-2), -4)

if __name__ == '__main__':
    unittest.main()
