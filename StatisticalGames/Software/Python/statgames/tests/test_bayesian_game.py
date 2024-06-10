# tests/test_fisher_game.py
import pytest

import numpy as np

try:
    # Try importing the package
    from statgames.bayesian_game import bayesiangame_solve
except ImportError:
    # If import fails, add the parent directory of the module to the Python path
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'statgames')))
    from bayesian_game import bayesiangame_solve


# pytest.approx(2/3, abs=1e-10)
def test_bayesiangame_solve():

    # Fisher games with integer coefficients

    # Trivial example
    # Zero game
    result = bayesiangame_solve(0, [0, 0], 0)
    assert result['P'] == 1/2
    assert result['P_interval'] == [1/2, 1/2]
    assert result['G'] == - np.log(2)
    assert result['p_prime'] == {0: 1/2}

    # Smallest nontrivial example
    result = bayesiangame_solve(1, [0, 1], 2, max_error=1e-12)
    assert result['P'] == pytest.approx(1/np.sqrt(5), abs=1e-12)
    assert result['P_interval'][1] - result['P_interval'][0] <= 2 * 1e-12
    assert result['P_interval'][0] == pytest.approx(1/np.sqrt(5), abs=2e-12)
    assert result['P_interval'][1] == pytest.approx(1/np.sqrt(5), abs=2e-12)
    assert result['G'] == pytest.approx( -np.log((3 + np.sqrt(5))/2) / 2, abs=1e-10)
    assert result['p_prime'][0] == pytest.approx((np.sqrt(5) - 1) / 2, abs=1e-10)
    assert result['p_prime'][1] == 0


if __name__ == '__main__':
    pytest.main()
