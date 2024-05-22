# tests/test_fisher_game.py
import unittest
from statgames.fisher_game import _fishergame_solve

class TestModule(unittest.TestCase):
    def test__fishergame_solve(self):
        self.assertEqual(_fishergame_solve(1,0,1,2)['P'], 2/3)
        self.assertEqual(_fishergame_solve(1,0,1,2)['k'], 0)
        self.assertEqual(_fishergame_solve(1,0,1,2)['nu'], 2/3)
        self.assertEqual(_fishergame_solve(1,0,1,2)['s'], 1/3)
        self.assertEqual(_fishergame_solve(1,0,1,2)['v'], 2/3)

if __name__ == '__main__':
    unittest.main()
