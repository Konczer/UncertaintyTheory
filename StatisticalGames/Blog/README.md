# Statistical Games, an informal summary


<img src="img/StatisticalGamesLogo.jpg" alt="StatisticalGamesLogo" width="100"/>

## Context

This is an informal introduction and summary of a longer manuscript on [Statistical Games](https://arxiv.org/abs/2402.15892), in a style of a technical blog post.
I intend to keep the material self contained in its message, but to bring the details closer to the interested readers I will often mention specific sections in the manuscript.
In this way the post can be viewed as a companion to the relatively long and technical document available on arXiv: 
[arXiv:2402.15892](https://arxiv.org/abs/2402.15892)

## Introduction

A virtually inavoidable task for every organism is to act based on partial information.
Humans, animals, machines all need to navigate in environments, where they can't see the full picture.

Although the incomprehensible complexity of the whole world prevents us from reaching absolute certainity, but we (various organisms) can construct models, gather data and develop heuristics to ride better the waves of reality.

One approach to refined heuristics is decision making based on statistics. However the most well known interpretations and frameworks for Probability theory and (theoretical-) Statistics seems to focus more on making rigorious statements (often in various limiting cases) then guiding an Agent having only a finite amount of data.

My aim was to construct a broader framework, where Statistics and Probability theory are not separate disciplines, operating with their own concepts, but where these are ingredients of a whole decision making process of an Agent, who needs to make moves having incomplete information.
After serious mathematical idealizations, by which we restrict the possible states of the environment and the Agent's possible actions, the best framework to analyse this decision making process appears to be Game Theory.


## Why Game Theory?

The concepts and techniques in Game Theory are in many cases compatible with decision making framework, while some parts needs adjustments.

### What is Game Theory?

<img src="img/GameTheoryLogo.png" alt="GameTheoryLogo" width="150"/>

Image source: [Introduction to Game Theory](https://nordstrommath.com/IntroGameTheoryv4-2020.pdf) a Discovery Approach by Jennifer Firkins Nordstrom

> The study of strategically interdependent behaviour.

[Game Theory](https://www.britannica.com/science/game-theory) is the formal description of *Games*, in which "rational" players can akt, and recieve payoffs based on their collective actions.



- There are finite number of Players
- Every Player can choose from (a possibly different) finite set of Actions
- Outcomes of the Game can depend on all Players chosen Action
- Players can NOT communicate with each other
- Players can "Randomize" their strategies, if desirable
- Players are "Rational", meaning they are aiming to maximize their [Expected Utility](https://plato.stanford.edu/entries/rationality-normative-utility/) 
- All above property (including every Players Action dependent Payoff) is Common Knowledge
    - meaning every Player knows, and every Player knows that every (other) Player knows, etc.

### What is NOT Game Theory?

There are a few frequent misconseptions to Game Theory, which I would address at this point:
"Game Theory assumes selfish players":
in the [dictionary sense](https://www.merriam-webster.com/dictionary/selfish): "concerned excessively or exclusively with oneself : seeking or concentrating on one's own advantage, pleasure, or well-being without regard for others" this is not the case. This is because any Player's utilities associated to possible outcomes is subjective, and can incorporate the welfare of other Players. For instance in any two-player game swapping the payoff functions of players would result a perfectly walid new game, in which both players are completely altruistic, concerned only about the others welfare.

"Game Theory is formalized Machiavellianism":
Again, if we take the [dictionary definition](https://www.merriam-webster.com/dictionary/Machiavellianism): "the view that politics is amoral and that any means however unscrupulous can justifiably be used in achieving political power",
then we see that Game Theory suggest Machiavellian strategies only if the Player's only concern is control and power. If the Player has other values, then this will change her strategies trough her utilities.

"Game Theory is grounded in Utilitarianism":
In Game Theory utility functions and utility matrices are subjective, personal and even their units ($\text{util}_1, \text{util}_2,\dots$) are not harmonized. This means thet the slogan of utilitarianism: "greatest good for the greatest number" is not automaticly compatible with the Game Theoretic framework. (Because adding the utilities of different agents does not respect the invariances which are present in Game Theory.)

"Game Theory can be used only for simple game of entertainment":
Unles the Expected Utility Hypothesis happens to be valid, a surpricingly wide variety of problems can be addressed by game theory. This includes social fields: Economics, Politics, Military theory, Sociology, etc. And non-humna related fields such as: Biology, Control theory, Artificial Intelligence (Reinforcement learning, Neural Networks), etc.

### Prototypical example:

Matching pennies:

$$
\underline{\underline{u}}_1=
\begin{bmatrix}
\textcolor{#E7A046}{\blacksquare} & \textcolor{#25548A}{\blacksquare} \\
\textcolor{#25548A}{\blacksquare} & \textcolor{#E7A046}{\blacksquare}
\end{bmatrix}, \quad
\underline{\underline{u}}_2=
\begin{bmatrix}
\textcolor{#25548A}{\blacksquare} & \textcolor{#E7A046}{\blacksquare} \\
\textcolor{#E7A046}{\blacksquare} & \textcolor{#25548A}{\blacksquare}
\end{bmatrix}
$$

$$
\textcolor{#E7A046}{\blacksquare} \succ_1 \textcolor{#25548A}{\blacksquare}, \quad
\textcolor{#E7A046}{\blacksquare} \succ_2 \textcolor{#25548A}{\blacksquare}
$$

$$
u_1(\textcolor{#E7A046}{\blacksquare}) >
u_1(\textcolor{#25548A}{\blacksquare}), \quad
u_2(\textcolor{#E7A046}{\blacksquare}) >
u_2(\textcolor{#25548A}{\blacksquare})
$$

### Decision making and Game Theory

In some sense a Decision making problem contains half of the information what a Game theoretic framework would require: the Decision maker knows her possible actions, has a model about possible "states of the world" and she knows her own preferences. What is missing for a definition of a game is the preferences of the other player.

Assuming that the world is animated by a "rational" player, and that it has preferences is of course fictional, and ment to be an analogy.
The usefulness of this metaphysical claim is not depending on primary on the forces and contituents of Nature (these are influencing the known parts of our models), but it can be judged based on the policies it suggests for the Decision maker.

### Game Theory and the concept of Probability

If we take the mentioned Matching Pennies game, or the more well known Rock-Paper-Scissors, then we can observe a very peculiar feature of the equilibrium strategies of these games.
The rules of these games are totally deterministic (no "device of chance" or any other "randomization" is involved), but they have no deterministic *pure* solutions. If there would be computable function governing one player's action, then the other player could predict her moves and win in every round.
Therefore searching for an equilibrium is paradoxical among deterministic (and computable) decision functions. The postulation of equilibrium strategies (by which most of the people have direct experience) needs the introduction of new kind of randomized *mixed* strategy, which is not deterministic and/or not predictible.

In some way this step of abstraction has some parallelles with the introduction of imaginary numbers. There we assumed that the equation $x^2=-1$ has roots, and termed them $\pm i$.

In the case of Matching Pennies we can also imagine (or postulate) that the game has an equilibrium solution, and say that in equilibrium both players are choosing Heads and Tails with *Probability* $0.5$.

$$
\Pr(H)=\Pr(T)=0.5
$$

One can ground the concept of probability and randomiztion for mixed strategies in other disciplines (which is often the case in standard introductory texts for Game Theory); however I am arguing that these simple games can serve as a sufficiently firm ground on which probability can be defined (or rather postulated).

As summarized by Ariel Rubinstein in [Comments on the Interpretation of Game Theory](http://dx.doi.org/10.2307/2938166):
> Mixed strategy can alternatively be viewed as the belief held by all other players concerning a player's actions. A mixed strategy equilibrium is then an $n$-tuple of common knowledge expectations, which has the property that all the actions to which a strictly positive probability is assigned are optimal, given the beliefs. A player's behavior may be perceived by all the other players as the outcome of a random device even though this is not the case.

Gregory Chaitin in a [conversation with Stephen Wolfram](https://youtu.be/d8MWRkS1pek?t=2004)

## Decision Theory and Uncertainty

<p align="center">
<img src="img/DALLEMetaPhysicsResearch.webp" alt="MetaPhysicsResearch" width="500" />
</p>
<center>Generated image by DALL·E to the prompt: "Metaphysics Research Lab"</center>

### Uncertainty

By uncertainty we will try to describe states, parameters or variables, to which we can associate possible values, but we can not associate probabilities in a credible way. In naming I will follow Frank Knight's seminal book from 1921: [Risk, uncertainty and profit](https://archive.org/details/riskuncertaintyp00knigrich/page/n5/mode/2up), in which Knight distinguishes Risk (where we can talk about probabilities) and Uncertainty (where not even the probabilities are known). For a more up to date summary I can suggest [Uncertainty in Economics](http://dx.doi.org/10.1007/978-3-319-55351-1) by Julia Köhn. (See a preview on [Google books](https://books.google.co.uk/books?id=AA4rDwAAQBAJ&printsec=frontcover&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false).)
In the literature uncertainty is often referred as ambiguity.

### Managing Uncertainty

We used a negative definition for uncertainty, it is a variable which can take some values, but we have no credible probability distribution which could characterize these possible values.
This can be a valid definition, but to manage or make decisions in the face of uncertainty it seems unavoidable to project some structure into these variables or draw some analogies with more familiar situations.

Contemplating on the nature of uncertainties is I think almost by definition a metaphysical endeavour (this explains the cover image for this section). This does not mean however that these problems are completely untractable, only that different frameworks can be judged primarely by their consequences manifesting in the agents' behaviour, and not by collecting empirical data about the world.

Choosing the appropriate criteria for behaviour, and judging their desaribality is of course a delicate matter, and maybe should remain subjective, but my aim is to show that some consequences of different metaphisical constructions can be determined, and reason for and against strategies in an educated way.



## Statistical Games

<p align="center">
<img src="img/StatisticalGames.png" alt="MetaPhysicsResearch" width="400" />
</p>

<center>

(Figure 6 in [arXiv:2402.15892](https://arxiv.org/abs/2402.15892))
</center>

### Aim of the paper

In the first part of the paper I simply posed a problem entirely in the framework of Game Theory, in which two players are playing a choosing-guessing game. By explicitly pstulating the preferences of the players, I avoided the problem of completing a decision meking problem with a fictional opponent and an imagined payoff matrix.

In these games players do not choose and guess only blindly, but the chooser (Player 2) needs to produce a finite binary sequence with given amount of $1$-s and $0$-s, while the guesser (Player 1) can sample a portion of the sequence and make her geuss based on the collected sample.

In the paper I intentionally chose the simplest possible construction, in which statistical concepts can first emerge. This has a downside, because the investigated problem can seem too simple for most real-world statistical problems. However by investigating the simplest toy model I was able to talk about statistical and probabilistic concepts without introducing any external stochastic (random) processes, and I was able to proove (or at leas conjecture) rigorous results for various limiting cases and deformations of the construction.

Therefore the main aim of the paper was to investigate a simple toy models in Game Theory, and use it as a proof of concept for using the framework to handle Decision making problems involving Uncertainty.

### A formal definition

To tie this informal summary closer to the actual manuscript, I though it is useful to explicitly spell aout the definitions of the central game constructions:

> **Definition 2.1** (Fisher game)**.** There are two players, Player 1 and Player 2.
Player 2 needs to choose between scenario A or B first and then produce a binary sequence of length $M$ containing precisely $K_A$ or $K_B$ number of $1$-s. (Without losing generality, we will assume $K_A \le K_B$.)
Following this, Player 1 (not knowing the actions of Player 2) can sample $N$ number of bits, and after observing their value, she guesses scenario A or B.
If Player 1 guessed the scenario correctly, she wins the game ($\textcolor{#E7A046}{\blacksquare}$) and loses otherwise ($\textcolor{#25548A}{\blacksquare}$). 
The above-defined Fisher game will be denoted as 
$\mathfrak{Game}(N, K_A, K_B, M)$.$♢$

