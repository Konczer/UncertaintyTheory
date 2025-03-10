# UncertaintyGameSolve

A [Wolfram Language](https://en.wikipedia.org/wiki/Wolfram_Language) (a.k.a. [Mathematica](https://www.wolfram.com/mathematica/)) package for computing the Extended Equilibrium for minimal Games with Uncertainty.

Based on the [arXiv:2503.01889](https://arxiv.org/abs/2503.01889) paper on *Non-Cooperative Games with Uncertainty*.

## Installation in Mathematica

You can install the package using `Get` or `<<` in Mathematica directly from the GitHub repository:

```Mathematica
Get["https://raw.githubusercontent.com/Konczer/UncertaintyTheory/refs/heads/main/ExtendedEqilibrium/Software/WL/UncertaintyGameSolve.m"]
```

## Uninstallation / Removal in Mathematica

If you need to uninstall / remove the package, you can do so by removing the defined functions in the contexts used in the package.

```Mathematica
Remove["UncertaintyGames`*"]
Remove["UncertaintyGames`Private`*"]
```

Alternatively you can always quit the kernel by using `Quit[]`, however, this will remove all defined functions and variables.

### Reinstallation in Mathematica

After removal, a repeated `Get` can cause the `::shdw` error message, if functions such as `MinimalUncertaintyGameSolve` remained in the ``Global` `` context. To avoid this use the following modified `Get` command:

```Mathematica
Remove[Global`MinimalUncertaintyGameSolve]
Get["https://raw.githubusercontent.com/Konczer/UncertaintyTheory/refs/heads/main/ExtendedEqilibrium/Software/WL/UncertaintyGameSolve.m"]
```

## Example notebook

An example [Mathematica](https://www.wolfram.com/mathematica/) notebook which uses `UncertaintyGameSolve` to reproduce results from the *Non-Cooperative Games with Uncertainty* paper is available on [GitHub](https://github.com/Konczer/UncertaintyTheory/blob/main/ExtendedEqilibrium/Software/WL/ExampleNotebook.nb).

To view the notebook withour [Wolfram Mathematica](https://www.wolfram.com/mathematica/) you can use the free [Wolfram Player](https://www.wolfram.com/player/), or to interact with it you can copy `UncertaintyGameSolve.m` to a [Wolfram Cloud](https://www.wolframcloud.com/) online notebook.

## Usage

The `MinimalUncertaintyGameSolve` function computes the Extended Equilibrium of minimal $|\mathcal{A}_1|=2$, $|\mathcal{A}_2|=2$, $|\Theta|=2$ games with uncertainty.

The structure of the input is the following:

$$
\text{\texttt{MinimalUncertaintyGameSolve[}} \langle \text{ \texttt{U1}}, \text{\texttt{U2} } \rangle \text{\texttt{]}} 
$$

where $\text{\texttt{U1}}$ and $\text{\texttt{U2}}$ are the utility arrays of the players. Using the definition and the notation from the [paper](https://arxiv.org/pdf/2503.01889#definition.3.1) these arrays are defined as follows:

$$
\text{\texttt{U1[[t,i,j]]}} := U_1((a_i,a_j);\theta_t)
$$

$$
\text{\texttt{U2[[t,i,j]]}} := U_2((a_i,a_j);\theta_t)
$$

### Generals and the Weather

Solving the [Generals and the Weather](https://arxiv.org/pdf/2503.01889#subsubsection.3.1.1) game from the paper:

```Mathematica
MinimalUncertaintyGameSolve[
    \[LeftAngleBracket]
    {{{1, 0}, {0, 1}}, {{1,0}, {1, 1}}}, 
    {{{0, 1}, {1, 0}}, {{0, 1}, {0, 0}}}
    \[RightAngleBracket]
    ]
```
Giving the output:

```Mathematica
{{"p" -> 1 - 1/Sqrt[2], "q" -> 2 - Sqrt[2], "P" -> 1/Sqrt[2], "Q" -> -1 + Sqrt[2]}}
```

Which corresponds to the Extended Equilibrium presented and checked in the [paper](https://arxiv.org/pdf/2503.01889#subsubsection.3.4.1).

### Coordination Game with Uncertain Payoffs

Solving a version of the [Battle of the Sexes game](https://en.wikipedia.org/wiki/Battle_of_the_sexes_(game_theory)) (also known as Bach or Stravinsky game), where the payoffs (or more precisely the utilities) depend from an uncertain parameter:

```Mathematica
MinimalUncertaintyGameSolve[
    \[LeftAngleBracket]
    {{{2, 0}, {0, 1}}, {{3,0}, {0, 1}}}, 
    {{{1, 0}, {0, 3}}, {{1, 0}, {0, 2}}}
    \[RightAngleBracket]
    ]
```

Giving the output:

```Mathematica
{
    {
        "p" -> 0, "q" -> 0
    }, 
    {
        "p" -> 1, "q" -> 1
    }, 
    {
        "p" -> 1/2 (5 - Sqrt[13]), "q" -> 1/2 (-3 + Sqrt[13]), 
        "P" -> 1/2 (5 - Sqrt[13]), "Q" -> 1/2 (-3 + Sqrt[13])
    }
}
```

Providing an example, where multiple Extended Equilibria exist.

## For developers

For interacting with a subdirectory of a Git repository see this [short summary](https://www.baeldung.com/ops/git-clone-subdirectory).

### Cloning

```bash
git clone --no-checkout --depth=1 https://github.com/Konczer/UncertaintyTheory.git
git checkout main -- ExtendedEqilibrium/Software/WL
```

## Citation

To cite the Mathematica package:

```latex
@software{UncertaintyGameSolve,
    title={UncertaintyGameSolve},
    author={Jozsef Konczer},
    year={2025},
    howpublished={GitHub. \url{https://github.com/Konczer/UncertaintyTheory/tree/main/ExtendedEqilibrium/Software/WL}},
    note={Mathematica script for solving games with uncertainty}
}
```

To cite the *Non-Cooperative Games with Uncertainty* paper, you can use the following BibTeX entry:

```latex
@misc{ExtandedEquilibriumKonczer2025,
      title={Non-Cooperative Games with Uncertainty}, 
      author={Jozsef Konczer},
      year={2025},
      eprint={2503.01889},
      archivePrefix={arXiv},
      primaryClass={econ.TH},
      url={https://arxiv.org/abs/2503.01889}, 
}
```