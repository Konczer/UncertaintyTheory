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