# tests/test_fisher_game.py
import pytest

try:
    # Try importing the package
    from statgames.fisher_game import fishergame_solve
except ImportError:
    # If import fails, add the parent directory of the module to the Python path
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'statgames')))
    from fisher_game import fishergame_solve



# pytest.approx(2/3, abs=1e-10)
def test_fishergame_solve():

    # Fisher games with integer coefficients

    # Trivial example
    # Zero game
    result = fishergame_solve(0, [0, 0], 0)
    assert result['P'] == 1/2
    assert result['k'] == 0
    assert result['nu'] == 1/2
    assert result['s'] == 1/2
    assert result['v'] == 1/2

    # Trivial example
    # N=0 Blind guessing
    result = fishergame_solve(0, [0, 0], 1)
    assert result['P'] == 1/2
    assert result['k'] == 0
    assert result['nu'] == 1/2
    assert result['s'] == 1/2
    assert result['v'] == 1/2

    # Trivial example
    # N=0 Blind guessing
    result = fishergame_solve(0, [0, 1], 1)
    assert result['P'] == 1/2
    assert result['k'] == 0
    assert result['nu'] == 1/2
    assert result['s'] == 1/2
    assert result['v'] == 1/2

    # Trivial example
    # N=0 Blind guessing
    result = fishergame_solve(0, [1, 1], 1)
    assert result['P'] == 1/2
    assert result['k'] == 0
    assert result['nu'] == 1/2
    assert result['s'] == 1/2
    assert result['v'] == 1/2

    # Trivial example
    # N=1 Blind guessing
    result = fishergame_solve(1, [0, 0], 1)
    assert result['P'] == 1/2
    assert result['k'] == 0
    assert result['nu'] == 1/2
    assert result['s'] == 1/4
    assert result['v'] == 1/2

    # Trivial example
    # Smallest Sure winning
    result = fishergame_solve(1, [0, 1], 1)
    assert 0 <= result['P'] <= 1
    assert result['k'] == 1
    assert result['nu'] == 0
    assert result['s'] == 1/2
    assert result['v'] == 1

    # Trivial example
    # N=2 Blind guessing
    result = fishergame_solve(1, [0, 0], 2)
    assert result['P'] == 1/2
    assert result['k'] == 0
    assert result['nu'] == 1/2
    assert result['s'] == 1/4
    assert result['v'] == 1/2

    # Smallest nontrivial example
    result = fishergame_solve(1, [0, 1], 2)
    assert result['P'] == 2/3
    assert result['k'] == 0
    assert result['nu'] == 2/3
    assert result['s'] == 1/3
    assert result['v'] == 2/3

    # Trivial example
    # Sure winning
    result = fishergame_solve(1, [0, 2], 2)
    assert 0 <= result['P'] <= 1
    assert result['k'] == 1
    assert result['nu'] == 0
    assert result['s'] == 1/2
    assert result['v'] == 1

    # Smallest nontrivial example, related case
    result = fishergame_solve(1, [1, 2], 2)
    assert result['P'] == 1/3
    assert result['k'] == 1
    assert result['nu'] == 1/3
    assert result['s'] == 2/3
    assert result['v'] == 2/3

    # Trivial example
    # N=2 Blind guessing
    result = fishergame_solve(1, [2, 2], 2)
    assert result['P'] == 1/2
    assert result['k'] == 1
    assert result['nu'] == 1/2
    assert result['s'] == 3/4
    assert result['v'] == 1/2

    # Binomial Fisher games with densities

    # Nintrivial example
    result = fishergame_solve(10, [0.3, 0.5])
    assert result['P'] == pytest.approx(0.4938830363664651, abs=1e-10)
    assert result['k'] == 4
    assert result['nu'] == pytest.approx(0.4405594510317179, abs=1e-10)
    assert result['s'] ==  pytest.approx(0.4036872228210653, abs=1e-10)
    assert result['v'] ==  pytest.approx(0.737775893831386, abs=1e-10)

if __name__ == '__main__':
    pytest.main()
