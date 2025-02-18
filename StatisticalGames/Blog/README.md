# Statistical Games, an informal summary


<img src="img/StatisticalGamesLogo.jpg" alt="StatisticalGamesLogo" width="100"/>

## Context

This is an informal introduction and summary of a longer manuscript on [Statistical Games](https://arxiv.org/abs/2402.15892).
I try to keep the material self-contained but to bring the paper closer, I will often mention specific sections and parts in the manuscript.
This blog post therefore aims to be a companion to the relatively long and more technical document available on arXiv.
For those who appreciate mathematical formalization, properly stated theorems and even proofs, I suggest to delve deeper to the actual paper:
[arXiv:2402.15892](https://arxiv.org/abs/2402.15892).

However, even if abstract formulas are not your cup of tee, in this post I tried my best to address the matter in a widely understandable way, so I encourige readers to carry on.

## Introduction

A practically unavoidable task for every organism is to act based on partial information.
Humans, animals, machines all need to navigate environments where they can't see the full picture.

Although the incomprehensible complexity of the whole world prevents us from reaching absolute certainty, we (and various other organisms) can construct models, gather data and develop heuristics to ride better the waves of reality.

One approach - which migh sound scientific and "objective" - used as a refined heuristics is decision-making aided with statistics. However, the most well-known interpretations and frameworks for [Probability theory](https://en.wikipedia.org/wiki/Probability_interpretations) and (theoretical-) [Statistics](https://plato.stanford.edu/entries/statistics/) seem to focus more on making rigorous statements (often only in various limiting cases) than guiding an Agent with only a finite amount of data.

My aim was to construct a broader framework where Statistics and Probability theory are not separate disciplines, operating with their own concepts, but where these are ingredients of an integrated decision-making process of an Agent who needs to make actions having incomplete information.
To construct a theory, mathematical idealisations has to be made - these will be discussed later - but after these simplifications the best framework to analyse this decision-making process appears to be [Game Theory](https://www.britannica.com/science/game-theory).

[comment]: <> (After substantial mathematical idealisations, - by which we restrict the possible states of the environment and the Agent's possible actions - the best framework to analyse this decision-making process appears to be [Game Theory](https://www.britannica.com/science/game-theory).)


## Why Game Theory?

The concepts and techniques in Game Theory are mostly compatible with the decision-making framework, but some essential parts need adjustments.

### What is Game Theory?

<img src="img/GameTheoryLogo.png" alt="GameTheoryLogo" width="150"/>

Image source: *[Introduction to Game Theory](https://nordstrommath.com/IntroGameTheoryv4-2020.pdf) a Discovery Approach* by Jennifer Firkins Nordstrom

A concise definition of Game Theory is:
> The study of strategically interdependent behaviour.

[Game Theory](https://www.britannica.com/science/game-theory) is the formal description of *Games*, in which "rational" players can act and receive payoffs based on their collective actions. Usually we start with the following assumptions:



- There are a finite number of Players
- Every Player can choose from (a possibly different) finite set of Actions
- Outcomes of the Game can depend on all Players' chosen Action
- Players can NOT communicate with each other
- Players can "randomise" their strategies if desirable
- Players are "rational", meaning they are aiming to maximise their *[Expected Utility](https://plato.stanford.edu/entries/rationality-normative-utility/)*
   - *utility* is the Players' subjective quantity associated to the possible consequences of the Game. (The theory does not restrict Players' utility judgements but they are assumed to be public i.e. known for all others.) 
- All above property (including every Players' action dependent payoffs or utilities) is *common knowledge*
    - meaning every Player knows, and every Player knows that every (other) Player knows, etc.

### What is NOT Game Theory?

There are a few frequent misconceptions about Game Theory, which I would address at this point:

- It is NOT the case that "Game Theory assumes selfish players":
    - In the [dictionary sense](https://www.merriam-webster.com/dictionary/selfish) of the meaning of "selfish":  "Concerned excessively or exclusively with oneself, seeking or concentrating on one's own advantage, pleasure, or well-being without regard for others". The definition is not a requirement for the Players in game theory. This is because any Player's utilities associated with possible outcomes are subjective and can incorporate other Players' welfare. For instance, swapping Players' payoff functions in any two-player game would result in a perfectly valid new game in which both players are completely altruistic and concerned only about the other Player's welfare.

- It is NOT the case that "Game Theory is formalised Machiavellianism":
    - Again, if we take the [dictionary definition](https://www.merriam-webster.com/dictionary/Machiavellianism): "The view that politics is amoral and that any means however unscrupulous can justifiably be used in achieving political power",
    then we see that game theory suggest Machiavellian strategies only if the Player's sole concern is control and power. If the Player has other values, this will change her strategy through her utilities.

- It is NOT the case that "Game Theory is grounded in Utilitarianism":
    - In Game Theory, utility functions and utility matrices are subjective, personal and even their units ($\text{util}_1, \text{util}_2,\dots$) are not authomaticly additive. This means that the [slogan of utilitarianism](https://plato.stanford.edu/entries/utilitarianism-history/): "greatest good for the greatest number", is not automatically compatible with the game theoretic framework. (Because adding the utilities of different Players does not respect the invariances present in the theory.)

- It is NOT the case that "Game Theory can be used only for pass time games of entertainment":
    - A surprisingly wide variety of problems can be addressed by game theory, until the Expected Utility Hypothesis holds. This includes social fields: Economics, Politics, Military theory, Sociology, etc. And non-human-related fields such as Biology, Control theory, Artificial Intelligence (Reinforcement Learning, Neural Networks), etc. (See a brief summary of uses on [Wikipedia](https://en.wikipedia.org/wiki/Game_theory#General_and_applied_uses), and related fields to Statistical Games in the ["Brief introduction"](https://arxiv.org/pdf/2402.15892#section.1).)

It is not a common misconception, but game theory is also not a universally valid and applicable description of human behaviour. [Allais paradox](https://en.wikipedia.org/wiki/Allais_paradox) showes that the expected utility assumption does not always describe well human decision making. Further culture and religion might have the power to not only shape the subjective utility functions of people (which would be still compatible with game theory), but to introduce new equilibrium concepts. [Berge equilibrium](https://en.wikipedia.org/wiki/Berge_equilibrium) can be viewed as the formalization of the [golden rule](https://en.wikipedia.org/wiki/Golden_Rule): "Treat others as you would like others to treat you." This equilibrium concept differs from the Nash equilibrium, and in general cannot be understood as simply the modification of utility functions.

Game theory is a rich and general framework, bit it does not automaticly describes all aspects of human - and perhaps other agents' - behaviour.

### Prototypical example:

Matching pennies:

<p align="center">
<img src="img/HandGameBones.jpg" alt="Hand Game Bones" width="400" />
</p>
<center>Hand Game Bone sticks https://americanindian.si.edu/collections-search/object/NMAI_20228 </center>


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

### Decision-making and Game Theory

In some sense, a Decision-making problem contains half of the information that a Game-theoretic framework would require: the Decision maker knows her possible actions, has a model about possible "states of the world" and knows her own preferences. What is missing from a definition of a game is the preferences of the other player.

Of course, assuming that the world is animated by a "rational" player and that it has preferences is fictional and meant to be an analogy.
The usefulness of this metaphysical claim does not depend primarily on the forces and constituents of Nature (these influence the known parts of our models), but it can be judged based on the policies it suggests for the decision-maker.

### Game Theory and the concept of Probability

If we take the mentioned Matching Pennies game or the more well-known Rock-Paper-Scissors game, we can observe a peculiar feature of their equilibrium strategies.
The rules of these games are totally deterministic (no "device of chance" or any other "randomisation" is involved), but they have no deterministic *pure* solutions. If there were a computable function governing one player's action, then the other player could predict her moves and win in every round.
Therefore, searching for an equilibrium is paradoxical among deterministic (and computable) decision functions. The postulation of equilibrium strategies (by which most people have direct experience) needs the introduction of a new kind of randomised *mixed* strategy that is not deterministic and/or predictable.

In some way, this step of abstraction has some parallels with the introduction of imaginary numbers. There, we assumed that the equation $x^2=-1$ has roots and termed them $\pm i$.

In the case of Matching Pennies, we can also imagine (or postulate) that the game has an equilibrium solution and say that in equilibrium, both players are choosing Heads and Tails with *Probability* $0.5$.

$$
\Pr(H)=\Pr(T)=0.5
$$

One can ground the concept of probability and randomization for mixed strategies in other disciplines (which is often the case in standard introductory texts for Game Theory); however, I am arguing that these simple games can serve as a sufficiently firm ground on which probability can be defined (or rather postulated).

As summarised by Ariel Rubinstein in [Comments on the Interpretation of Game Theory](http://dx.doi.org/10.2307/2938166):
> Mixed strategy can alternatively be viewed as the belief held by all other players concerning a player's actions. A mixed strategy equilibrium is then an $n$-tuple of common knowledge expectations, which has the property that all the actions to which a strictly positive probability is assigned are optimal, given the beliefs. A player's behavior may be perceived by all the other players as the outcome of a random device, even though this is not the case.

Gregory Chaitin in a [conversation with Stephen Wolfram](https://youtu.be/d8MWRkS1pek?t=2004)

## Decision Theory and Uncertainty

<p align="center">
<img src="img/DALLEMetaPhysicsResearch.webp" alt="MetaPhysicsResearch" width="500" />
</p>
<center>Generated image by DALL·E to the prompt: "Metaphysics Research Lab"</center>

### Uncertainty

By uncertainty, we will try to describe states, parameters or variables to which we can associate possible values, but we can not associate probabilities in a credible way. In naming, I will follow Frank Knight's seminal book from 1921: [Risk, uncertainty and profit](https://archive.org/details/riskuncertaintyp00knigrich/page/n5/mode/2up), in which Knight distinguishes Risk (where we can talk about probabilities) and Uncertainty (where not even the probabilities are known). I can suggest [Uncertainty in Economics](http://dx.doi.org/10.1007/978-3-319-55351-1) for a more up-to-date summary by Julia Köhn. (See a preview on [Google Books](https://books.google.co.uk/books?id=AA4rDwAAQBAJ&printsec=frontcover&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false).)
In the literature, uncertainty is often referred to as ambiguity.

### Managing Uncertainty

We used a negative definition for uncertainty, a variable that can take some values, but we have no credible probability distribution that could characterise these possible values.
This can be a valid definition, but to manage or make decisions in the face of uncertainty, it seems unavoidable to project some structure into these variables or draw some analogies with more familiar situations.

Contemplating the nature of uncertainties is, I think, almost by definition a metaphysical endeavour (this explains the cover image for this section). This does not mean, however, that these problems are completely untractable, only that different frameworks can be judged primarily by their consequences manifesting in the agents' behaviour and not by collecting empirical data about the world.

Choosing the appropriate criteria for behaviour and judging its desirability is a delicate matter and may need to remain subjective. Still, my aim is to show that some consequences of different metaphysical constructions can be determined and to reason for and against strategies in an educated way.



## Statistical Games

<p align="center">
<img src="img/StatisticalGames.png" alt="MetaPhysicsResearch" width="400" />
</p>

<center>

(Figure 6 in [arXiv:2402.15892](https://arxiv.org/abs/2402.15892))
</center>

### Aim of the paper

In the first part of the paper, I simply posed a problem entirely in the framework of Game Theory: Two players are playing a choosing-guessing game. By explicitly postulating the players' preferences, I avoided the problem of completing a decision-making problem with a fictional opponent and an imagined payoff matrix.

In these games, players do not choose and guess blindly. The chooser (Player 2) needs to produce a finite binary sequence with a given amount of $1$-s and $0$-s, while the guesser (Player 1) can sample a portion of the sequence and make her guess based on the collected sample.

In the paper, I intentionally chose the simplest possible construction in which statistical concepts can first emerge. This has a downside because the investigated problem can seem too simple for most real-world statistical problems. However, by investigating the simplest toy model, I was able to talk about statistical and probabilistic concepts without introducing any external stochastic (random) processes, and I was able to prove (or at least conjecture) rigorous results for various limiting cases and deformations of the construction.

Therefore, the main aim of the paper was to investigate a simple toy model in Game Theory and use it as a proof of concept for using the framework to handle decision-making problems involving Uncertainty.

### A formal definition

To tie this informal summary closer to the actual manuscript, I thought it would be useful to spell out the definitions of the central game constructions explicitly:

> **Definition 2.1** (Fisher game)**.** There are two players, Player 1 and Player 2.
Player 2 needs to choose between scenario A or B first and then produce a binary sequence of length $M$ containing precisely $K_A$ or $K_B$ number of $1$-s. (Without losing generality, we will assume $K_A \le K_B$.)
Following this, Player 1 (not knowing the actions of Player 2) can sample $N$ number of bits, and after observing their value, she guesses scenario A or B.
If Player 1 guessed the scenario correctly, she wins the game ($\textcolor{#E7A046}{\blacksquare}$) and loses otherwise ($\textcolor{#25548A}{\blacksquare}$). 
The above-defined Fisher game will be denoted as 
$\mathfrak{Game}(N, K_A, K_B, M)$.$♢$

In a less formal language:

> In **Fisher games**, a Chooser player (Player 2) needs to choose from two distinct sets of binary sequences, A or B, while the Guessing player (Player 1) can sample from the sequence and then needs to guess if the sample came from A or B.
The Guessing player wins if she guesses correctly.
Fisher games are described by four additional integers: the length of the whole binary sequences $M$, the total number of 1-s in the sequences in A $K_A$, the total number of 1-s in the sequences in B $K_B$, and the number of bits the Guessing player can sample from the chosen sequence $N$.
This game will be denoted as $\mathfrak{Game}(N, K_A, K_B, M)$.

