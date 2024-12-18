# statgames

A package for calculating equilibrium quantities for Fisher, Bayesian, and Statistical Games.

Based on the [arXiv:2402.15892](https://arxiv.org/abs/2402.15892) paper on Statistical Games.

## Dependencies

This package requires `numpy`, `scipy`.

## Installation

You can install the package using pip directly from the GitHub repository:

```bash
pip install git+https://github.com/Konczer/UncertaintyTheory.git@main#subdirectory=StatisticalGames/Software/Python/statgames
```

## Uninstallation

If you need to uninstall the package, you can do so using pip. Run the following command in your terminal:

```bash
pip uninstall statgames
```

## Example notebook

An example Jupyter notebook which uses `statgames` to reproduce figures from the [Statistical Games](https://arxiv.org/pdf/2402.15892) paper is available on [GitHub](https://github.com/Konczer/UncertaintyTheory/blob/main/StatisticalGames/Notebooks/Jupyter/StatisticalGames.ipynb) and an interactive version on [Google Colab](https://colab.research.google.com/drive/1dFSqVPMd0_6Ai8iMfoohOETQjdy2C2GD?usp=sharing).

## Usage

### Fisher Game

The `fishergame_solve` function solves a Fisher game and calculates equilibrium quantities.

**Example Usage:**

Solving a Fisher game with finite `M`:

$\mathfrak{Game}(N=1, K_A=0, K_B=1, M=2)$:
```python
from statgames import fishergame_solve

result = fishergame_solve(1, [0, 1], 2)
print(result)
# Output: { 'P': 0.6666666666666666, 
#           'k': 0, 
#           'nu': 0.6666666666666666, 
#           's': 0.3333333333333333, 
#           'v': 0.6666666666666666
#           }
```

Solving a Fisher game with infinite `M` i.e. a Binomial Fisher game:

$\overline{\mathfrak{Game}}(N=10, x_A=0.3, x_B=0.5)$:
```python
from statgames import fishergame_solve

result = fishergame_solve(10, [0.3, 0.5])
print(result)
# Output: {'P': 0.4938830363664651, 
#          'k': 4, 
#           'nu': 0.4405594510317179, 
#           's': 0.4036872228210653, 
#           'v': 0.737775893831386
#           }
```

### Bayesian Game

The `bayesiangame_solve` function solves a Bayesian game and calculates equilibrium quantities.

**Example Usage:**

Solving a Bayesian game with finite `M`:

$\mathfrak{BGame}(N=1, K_A=0, K_B=1, M=2)$:
```python
from statgames import bayesiangame_solve

result = bayesiangame_solve(1, [0, 1], 2)
print(result)
# Output: {
#      'P': 0.4462890625, 
#      'P_interval': [0.4462890625, 0.447265625], 
#      'G': -0.4812106300819732, 
#      'p_prime': {
#           0: 0.6171505739365294, 
#           1: 0.0
#           }
#       }
```

Solving the Bayesian game with infinite `M` i.e. a Binomial Bayesian game:

$\overline{\mathfrak{BGame}}(N=10, x_A=0.3, x_B=0.5)$:
```python
from statgames import bayesiangame_solve

result = bayesiangame_solve(10, [0.3, 0.5])
print(result)
# Output: {
#    'P': 0.4990234375, 
#    'P_interval': [0.498046875, 0.5], 
#    'G': -0.5158309498018485, 
#    'p_prime': {
#        0: 0.9664572431930976, 
#        1: 0.925084082646245, 
#        2: 0.8410712502801064, 
#        3: 0.6940075752961667, 
#        4: 0.49290664335788936, 
#        5: 0.29407520178603835, 
#        6: 0.15148886921226545, 
#        7: 0.07107654724506647, 
#        8: 0.03175094751718913, 
#        9: 0.013858998265404298, 
#        10: 0.005986984172753379
#        }
#    }
```

### Statistical Game

The `statisticalgame_solve` function solves a Statistical game and calculates equilibrium quantities.

**Example Usage:**

Solving a Statistical game with finite `M`:

$\mathfrak{SGame}(N=1, K_A=0, K_B=1, M=2, \gamma=0.5)$:
```python
from statgames import statisticalgame_solve

result = statisticalgame_solve(1, [0, 1], 2, gamma=0.5)
print(result)
# Output: {
#      'P': 0.3994140625, 
#      'P_interval': [0.3984375, 0.400390625], 
#      'U': -0.3999993129521612, 
#      'p_prime': {
#           0: 0.6388739570095546, 
#           1: 0.0
#           }
#       }
```

Solving the Statistical game with infinite `M` i.e. a Binomial Statistical game:

$\overline{\mathfrak{SGame}}(N=10, x_A=0.3, x_B=0.5, \gamma=0.5)$:
```python
from statgames import statisticalgame_solve

result = statisticalgame_solve(10, [0.3, 0.5], gamma=0.5)
print(result)
# Output: {
#    'P': 0.4951171875, 
#    'P_interval': [0.494140625, 0.49609375], 
#    'U': -0.38742895605774774, 
#    'p_prime': {
#        0: 0.9987587334732929, 
#        1: 0.9932790709733905, 
#        2: 0.9644695967162675, 
#        3: 0.832937947072644, 
#        4: 0.4780137141353738, 
#        5: 0.14398267774885304, 
#        6: 0.02996816223631757, 
#        7: 0.00564239067955681, 
#        8: 0.0010411530573117144, 
#        9: 0.0001913948646887022, 
#        10: 3.515965218925e-05
#        }
#    }
```

## For developers

For interacting with a subdirectory of a Git repository see this [short summary](https://www.baeldung.com/ops/git-clone-subdirectory).

### Cloning

```bash
git clone --no-checkout --depth=1 https://github.com/Konczer/UncertaintyTheory.git
git checkout main -- StatisticalGames/Software/Python/statgames
```

## Citation

To cite the Python package:

```
@software{statgames,
    title={statgames},
    author={Jozsef Konczer},
    year={2024},
    howpublished={GitHub. \url{https://github.com/Konczer/UncertaintyTheory/tree/main/StatisticalGames/Software/Python/statgames}},
    note={Software for Statistical Games in Python}
}
```

To cite the Statistical Games paper:

```latex
@misc{konczer2024statisticalgames,
    title={Statistical Games}, 
    author={Jozsef Konczer},
    year={2024},
    eprint={2402.15892},
    archivePrefix={arXiv},
    primaryClass={math.ST}
}
```