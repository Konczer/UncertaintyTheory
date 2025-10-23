# Statistical Games, an informal summary


<img src="img/StatisticalGamesLogo.jpg" alt="StatisticalGamesLogo" width="100"/>

## Context

This is an informal introduction and summary of a longer manuscript on [Statistical Games](https://arxiv.org/abs/2402.15892).
I try to keep the material self-contained, but to bring the paper closer, I will often mention specific parts and sections in the original document.
This blog post, therefore, aims to serve as a companion to the relatively long, more technical preprint available on arXiv.
For those who appreciate mathematical formalisation, properly stated theorems and even proofs, I suggest delving deeper into the actual paper:
[arXiv:2402.15892](https://arxiv.org/abs/2402.15892) and/or visit the paper's [GitHub page](https://github.com/Konczer/UncertaintyTheory/tree/main/StatisticalGames).

However, even if abstract formulas are not your cup of tea, in this post, I tried my best to address the matter in a widely understandable way, so I encourage readers to carry on.

Further, if you prefer starting to read immediately the summary of the paper and not engaging with the relatively lengthy philosophical and cultural embedding of the work to a greater project, then I suggest jumping immediately to the **Statistical Games** section below.

## Introduction

A practically unavoidable task for every organism is to act based on partial information.
Humans, animals, machines all need to navigate environments where they can't see the full picture.

Although the incomprehensible complexity of the whole world prevents us from reaching absolute certainty, we (and various other organisms) can construct models, gather data and develop heuristics to ride "better" the waves of reality.

One approach - which might sound scientific and "objective" - used as a refined heuristic is decision-making aided by statistics and probability theory. However, the most well-known interpretations and frameworks for [Probability theory](https://en.wikipedia.org/wiki/Probability_interpretations) and (theoretical-) [Statistics](https://plato.stanford.edu/entries/statistics/) seem to focus more on making rigorous statements (often only in various limiting cases) than guiding an Agent with only a finite amount of data.

My aim was to construct a broader framework in which Statistics and Probability theory are not separate disciplines operating with their own concepts, but are ingredients in an integrated decision-making process for an Agent that needs to take actions with incomplete information.
To construct a theory, mathematical idealisations have to be made - these will be discussed later - but after these simplifications, the best framework to analyse this decision-making process appears to be [Game Theory](https://www.britannica.com/science/game-theory).


## Why Game Theory?

The concepts and techniques in Game Theory are mostly compatible with the decision-making framework, but some essential parts need adjustments.
(Most profoundly, one has to construct by the force of imagination a fictional opponent in uncertain situations, where there might be no other, only we and our doubts.)

### What is Game Theory?

<img src="img/GameTheoryLogo.png" alt="GameTheoryLogo" width="150"/>

Image source: *[Introduction to Game Theory](https://nordstrommath.com/IntroGameTheoryv4-2020.pdf) a Discovery Approach* by Jennifer Firkins Nordstrom

A concise definition of Game Theory is:
> The study of strategically interdependent behaviour.

To be a little more concrete, one can first think of rock-paper-scissors, board games, or any leisure game with fixed rules and well-defined possible moves.
(However, the formalism of Game Theory is much more widely applicable than recreational games. After a necessary reductive modelling step, it can be used to address problems in biology, politics, economy, military and more.)

[Game Theory](https://www.britannica.com/science/game-theory) is the formal description of *Games*, in which "rational" players can act and receive payoffs based on their collective actions. (I wish to distinguish a lowercase real game from its abstract mathematical model, the upper case Game. The formal Game is an idealized - and often simplified - mathematical object in Game Theory containing not only the formalized rules of the game but also the quantitative incentives of the assumed idealized players, playing the game.) Usually, we start with the following assumptions:

- There is a finite number of Players
- Every Player can choose from (a possibly different) finite set of Actions
- Outcomes of the Game can depend on all Players' chosen Actions
- Players can NOT communicate with each other (outside the Game)
- Players can "randomise" their strategies if desirable
- Players are "rational", meaning they are aiming to maximise their *[Expected Utility](https://plato.stanford.edu/entries/rationality-normative-utility/)*
   - *Utility* is the Players' subjective quantity associated with the "desirability" of possible consequences of the Game. (The theory does not restrict Players' Utility judgments, but they are assumed to be public, i.e., known to all others.) 
- All above properties (including every Player's action-dependent payoffs or utilities) are *common knowledge*
    - meaning every Player knows, and every Player knows that every (other) Player knows, etc.

### What is NOT Game Theory?

There are a few frequent misconceptions about Game Theory, which I would address at this point:

 - It is NOT the case that "Game Theory assumes selfish players":
    - "Selfishness" - in the [dictionary sense](https://www.merriam-webster.com/dictionary/selfish) - "Concerned excessively or exclusively with oneself, seeking or concentrating on one's own advantage, pleasure, or well-being without regard for others" is not baked into Game Theory.
    This is because any Player's Utilities associated with possible outcomes are subjective and can incorporate other Players' preferences.
    Formally, for instance, swapping two Players' payoff functions in a Game would result in a perfectly valid new formal Game' in which the rules are the same, but both players are entirely altruistic and concerned only about the other Player's (original) welfare.
    In other words, the first part of the definition "Concerned excessively or exclusively with oneself" is assumed in the formalisation, but the freedom of adopting any utility function allows for altruistic or more wise outlooks. 
    This flexibility of the utility function - by allowing the Players to contemplate their personal virtues - opens the door in the formalism to a basic form of wisdom and allows transcending self-centred and short-sighted strategies.


- It is NOT the case that "Game Theory is formalised Machiavellianism":
    - Again, if we take the [dictionary definition](https://www.merriam-webster.com/dictionary/Machiavellianism) for Machiavellianism: "The view that politics is amoral and that any means, however unscrupulous can justifiably be used in achieving political power",
 then we see that game theory suggests Machiavellian strategies only if the Player's sole concern is control and power. If the Player has other values, this will change her strategy through her subjective utilities.

 - It is NOT the case that "Game Theory is promoting zero-sum thinking":
    - Although zero-sum games were important in the early development of Game Theory, the general structure suits both conflicting and aligned players, i.e. competitive and cooperative behaviour.
    Therefore, the framework is applicable to navigate and recognise [non-zero-sum](https://en.wikipedia.org/wiki/Nonzero:_The_Logic_of_Human_Destiny) opportunities, and it can be used to create and stabilise cooperative behaviour. (In fact, [Mechanism Design](https://en.wikipedia.org/wiki/Mechanism_design) - a branch of Game Theory - can be viewed as the art of designing rules and incentive structures to create or enhance cooperative - or otherwise desired - behaviour.)
    
- It is NOT the case that "Game Theory is grounded in Utilitarianism":
    - In Game Theory, utility functions and utility matrices are subjective, personal, and even their units ($\text{util}_1, \text{util}_2,\dots$) are not automatically additive. This means that the [slogan of utilitarianism](https://plato.stanford.edu/entries/utilitarianism-history/): "greatest good for the greatest number", is not automatically compatible with the game theoretic framework. (Formally, because adding the utilities of different Players does not respect the invariances otherwise present in the theory - saying simply, adding different Player's utilities together does not make sense in Game Theory.)
    

- It is NOT the case that "Game Theory can be used only for pastime games of entertainment":
    - A surprisingly wide variety of problems can be addressed by Game Theory, as long as the Expected Utility Hypothesis holds. This includes social fields such as Economics, Politics, Military theory, Sociology, etc. And non-human-related fields such as Biology, Control theory, Artificial Intelligence (Reinforcement Learning, Neural Networks), etc. (See a brief summary of uses on [Wikipedia](https://en.wikipedia.org/wiki/Game_theory#General_and_applied_uses), and related fields to Statistical Games in the ["Brief introduction"](https://arxiv.org/pdf/2402.15892#section.1).)

- It is NOT the case that "Game Theory is the ultimate guide for life":
    - There are genuine limitations of Game Theory that prevent it from becoming an overarching framework for life.
    The formalism assumes fixed preferences; therefore, it cannot handle changing preferences of the Players, whether the change is spontaneous or induced by some actions, during the Game. Further, the separate identity of the Players is also ingrained in the formalism. Therefore, Players are assumed to be eternal with never-changing preferences in the state of separation from each other and from the world as a whole (except by their narrow actions and their consequences). 
    (Generalizations of the theory exist, e.g., [Bayesian games](https://en.wikipedia.org/wiki/Bayesian_game), where Players can have previously unknown "types", potentially influencing their preferences; [Correlated equilibrium](https://en.wikipedia.org/wiki/Correlated_equilibrium), where some "signalling" among Players is allowed, etc. However, in general, no simple refinement seems to address all important aspects of the living experience.)
    Game Theory is flexible enough to provide a valuable model-making tool for a wide variety of "strategically interdependent behaviours". Still, I would suggest against relying on one's life decisions and moral/ethical outlook solely on it.


It might not be a common misconception, but Game Theory is also not a universally valid and applicable description of human behaviour. For instance, the [Allais paradox](https://en.wikipedia.org/wiki/Allais_paradox) shows that the expected utility assumption does not always describe well human decision-making. Further, culture and religion might have the power to not only shape the subjective utility functions of people (which would still be compatible with game theory), but also introduce new equilibrium concepts. [Berge equilibrium](https://en.wikipedia.org/wiki/Berge_equilibrium) can be viewed as the formalisation of the [golden rule](https://en.wikipedia.org/wiki/Golden_Rule): "Treat others as you would like others to treat you." This equilibrium concept differs from the Nash equilibrium and, in general, cannot be understood as simply a modification of utility functions.

These were only two arbitrary examples from a bulk of evidence that indicate that Game Theory is not the ultimate descriptive theory of human - and perhaps other kinds of Agents' - behaviour.

Game theory is a rich and flexible general framework. But perhaps not everything should be forced into its mould.

### Prototypical example:

The so-called **Matching pennies** is perhaps the simplest two-player game.
I picked the Native American [Hand Game](https://en.wikipedia.org/wiki/Handgame) - with prehistoric roots - as a concrete illustrative example.

One round looks as follows: the game is played by two sides, the *Guessing* (Player 1) and the *Hiding* (Player 2) players.
There are two pairs of "Bones" (see illustration below), each pair consisting of one plain and one striped bone.
The *Hiding* player has to hide the stripped bone in her left or right hand (while putting the plain bone in the other hand). And the *Guessing* player has to guess which hand the stripped bone is hidden in.

If the *Guessing* player guessed correctly, she wins the round and loses otherwise.

<p align="center">
  <img src="img/HandGameBones.jpg" alt="Hand Game Bones" width="400">
</p>
<p align="center">
  <em>
    Hand Game Bone sticks (image from 
    <a href="https://americanindian.si.edu/collections-search/object/NMAI_20228" target=_blank>National Museum of the American Indian</a>).
  </em>
</p>

(It is worth mentioning that the full form of this game was not only a pastime activity, but it was also used to settle disputes and conflicts among individuals and groups.)

Without any formal reasoning, I think it is clear that the best strategy for the *Hiding* player is to choose her hiding hand randomly (i.e. as unpredictably as possible) without any bias towards left or right. (This is how she can confuse the *Guessing* player the most and protect herself from exploitation.)
While the best strategy for the *Guessing* player remains to guess randomly and uniformly between left and right. (Essentially for the same reasons as the *Hiding* player.)

Now let's see how this simple game can be formalised in the language of Game Theory.

There are two players, Player 1 (the *Guessing* player) and Player 2 (the *Hiding* player). Both of them having "Action sets" $\mathcal{A}_1=\{\text{Left}, \text{Right}\}$ and $\mathcal{A}_2=\{\text{Left}, \text{Right}\}$ respectively.
(For Player 1, the actions mean that she can guess Left or Right, while for Player 2, the actions mean that she can hide the stripped bone in her Left or Right hand.)

There are two players, Player 1 (the *Guessing* player) and Player 2 (the *Hiding* player). Both of them having "Action sets" $\mathcal{A}_1=\&lbrace;\text{Left}, \text{Right}\&rbrace;$ and $\mathcal{A}_2=\&lbrace;\text{Left}, \text{Right}\&rbrace;$ respectively.
(For Player 1, the actions mean that she can guess Left or Right, while for Player 2, the actions mean that she can hide the stripped bone in her Left or Right hand.)


Player 1 wins - and Player 2 loses - if both choose Right or both choose Left. Victory is denoted by $\textcolor{#E7A046}{\blacksquare}$. If the chosen and guessed hands differ, then Player 1 loses ($\textcolor{#25548A}{\blacksquare}$) - and Player 2 wins.

The Hand Game is only one example that can be formally identified with [Matching Pennies](https://en.wikipedia.org/wiki/Matching_pennies) (I chose it to emphasise how deeply ingrained such games are in human cultures).
In its "canonical" definition, the two players are usually called Even (Player 1) and Odd (Player 2), and their possible actions - which they can make independently and secretly - are choosing Heads or Tails ($\mathcal{A}_1=\mathcal{A}_2=\{H,T\}$). If the pennies match (both Heads or both Tails), then Even wins; and if the pennies do not match (one Heads and one Tails), then Odd wins.

(Another almost identical game is called [Odds and evens](https://en.wikipedia.org/wiki/Odds_and_evens_(hand_game)), but there are multiple situations in real life which such simple simultaneous choosing-guessing games can model. [Penalty kicks](https://blogs.cornell.edu/info2040/2022/09/21/the-game-theory-of-soccer-penalty-kicks/) in football (also known as soccer) being one of the [well-studied](http://www.palacios-huerta.com/docs/professionals.pdf) cases.)
In the Statistical Games paper, the [Blind guessing](https://arxiv.org/pdf/2402.15892#subsubsection.2.1.1), a "maximally trivial" version of the general guessing game corresponds to the Matching Pennies. 

In game theory, we capture the essence of a game in a *utility matrix*, which is a table of outcomes for each player, where rows represent the actions of Player 1 and columns the actions of Player 2.
For the Matching Pennies, the utility matrices are simple two-by-two tables:

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

In standard Game Theory, the entries of the utility matrices are usually real numbers, measuring some level of "desirability" of a given outcome for a given player, but often the specific numerical values do not change the optimal strategies of the players. This is the case here. The optimal strategies are the same unless both players *prefer* winning $\textcolor{#E7A046}{\blacksquare}$ over losing $\textcolor{#25548A}{\blacksquare}$.
In formal notation, this would mean:

$$
\textcolor{#E7A046}{\blacksquare} \succ_1 \textcolor{#25548A}{\blacksquare}, \quad
\textcolor{#E7A046}{\blacksquare} \succ_2 \textcolor{#25548A}{\blacksquare}
$$

Or by introducing numerical utility functions $\text{u}_1$, $\text{u}_2$ (associating a real valued "desirability" to the abstract winning ($\textcolor{#E7A046}{\blacksquare}$) and losing ($\textcolor{#25548A}{\blacksquare}$) statuses) for Player 1 and Player 2 respectively:

$$
\text{u}_1(\textcolor{#E7A046}{\blacksquare}) >
\text{u}_1(\textcolor{#25548A}{\blacksquare}), \quad
\text{u}_2(\textcolor{#E7A046}{\blacksquare}) >
\text{u}_2(\textcolor{#25548A}{\blacksquare})
$$

As a somewhat unusual note, I would add that the formal structure of the theory allows for an incentive structure in which one player - for example, Player 2 - wishes the other players victory more than her own (while Player 1 still prefers to win the game). This would change the Game - in game theory, Games are defined together with explicit utility matrices- from a Matching Pennies to a [Coordination Game](https://en.wikipedia.org/wiki/Coordination_game), in which always choosing the same action (Left or Right) is an optimal strategy for both players. (The lack of communication can hinder the coordination - this is why even such fully aligned interaction might be tricky -, which causes an extra unfortunate but equilibrial strategy. However, this will not be important for the following discussion, so I will stop discussing the matter here.)
The point I want to make is that the players' subjective preferences can influence the behaviour of all interacting agents and the set of possible equilibria.

Despite its simplicity, I claim that this prototypical Game captures an essential insight that can be generalised and expanded into a general theory of decision-making under uncertainty, and, with that, provides an alternative grounding for statistics and potentially probability theory.

### Game Theory and the concept of Probability

If we take the mentioned Matching Pennies Game (alternatively, one can think of the more widely-played Rock-Paper-Scissors), we can observe a peculiar feature of their equilibrium strategies.
The rules of these games are totally deterministic (no "device of chance" or any other "randomisation" is involved), but they have no deterministic *pure* solutions. If there were a computable function governing one player's action, then the other player could predict her moves and win in every round.
Therefore, searching for an equilibrium is paradoxical among deterministic (and computable) decision functions. The postulation of equilibrium strategies (by which most people have direct experience) needs the introduction of a new kind of randomised *mixed* strategy that is not deterministic and/or predictable.

In a sense, this step of abstraction has some parallels with the introduction of imaginary numbers. There, we assumed that the equation $x^2=-1$ has roots and termed them $i$ and $-i$, the positive and negative imaginary unit. The fruits of this bold move are that it helps express solutions to any polynomial and that it simplifies the calculation of many mathematical problems, including those involving only real numbers, both in their definitions and in their solutions. (A classic example, in algebra is the ["Casus irreducibilis"](https://en.wikipedia.org/wiki/Casus_irreducibilis)).

The power of imagination can help us not only in algebra but also in decision-making problems.
In the case of Matching Pennies, we can also imagine (or postulate) that the game has an equilibrium solution and - to emphasise that choosing between the two options should be unbiased - say that in equilibrium, both players are choosing Heads and Tails with *Probability* $1/2=0.5$.

$$
\Pr(H)=\Pr(T)=1/2=0.5
$$

One can ground the concepts of probability and randomisation for mixed strategies in other disciplines (which is often the case in standard introductory texts on Game Theory); however, I argue that these simple games can serve as sufficiently firm ground on which probability can be defined (or rather postulated).

As summarised - in a bit technical but profoundly accurate way - by Ariel Rubinstein in [Comments on the Interpretation of Game Theory](http://dx.doi.org/10.2307/2938166):
> Mixed strategy can alternatively be viewed as the belief held by all other players concerning a player's actions. A mixed strategy equilibrium is then an $n$-tuple of common knowledge expectations, which has the property that all the actions to which a strictly positive probability is assigned are optimal, given the beliefs. A player's behaviour may be perceived by all the other players as the outcome of a random device, even though this is not the case.

In fact, John von Neumann himself spent the whole *17. Mixed Strategies* part in the [Theory of Games and Economic Behavior](https://archive.org/details/in.ernet.dli.2015.215284) to discuss the nuances of the concept of randomisation in Game Theory.
I think the thoughts of Gregory Chaitin on the matter are also worth linking:
[Gregory Chaitin in a conversation with Stephen Wolfram](https://youtu.be/d8MWRkS1pek?t=2004)  (however, I have to note that I wasn't able to find the mentioned footnote by Neumann in the original book).

In my view, both Neumann and Chaitin realised that Game Theory is intimately linked to randomisation and probability. Traditional approaches aim to ground optimal mixed strategies in games with some other, more physical or mechanistic notion of randomisation (like dice, coins, or computation). 
I wish to flip the script and, instead of searching for a probabilistic model (borrowed from an independent framework) to describe Game Theory, I propose grounding the concepts of probability and various statistical heuristics in our experience and intuition about games and their equilibria.

In a way, I propose that statistics can be viewed as mapping real-world situations to simple - or at least formal - Games, and then using our experience and intuition about games to guide our decisions (potentially aided by some computation to avoid getting lost in the combinatorial explosion of possibilities).


### Formal definition of Equilibrium

In Game Theory, there is a formal definition for a strategy - or more precisely a set of strategies for all Players - which captures the concept intuitively understood as optimal play. A set or profile of strategies is called an *equilibrium* if all players are adopting a strategy that maximizes their gains - their expected utility - given the strategies of all other Players.
It might sound like a circular definition at first - given that in a typical game, the other players' strategies influence one's own best responses in a given situation - but both mathematically and intuitively, such collective strategies can be found.

<p align="center">
  <img src="img/RecursiveSculpture.jpg" alt="Recursive sculpture" width="500">
</p>
<p align="center">
  <em>
    Sculpture: Sigmund (talking to Sigmund, talking to Sigmund, talking to Sigmund...) by Michal Gabriel in Jinačovice, near Brno, Czech Republic (not far from Freiberg (Příbor), Freud's birth-town). 
    <a href="https://www.facebook.com/ObcojezycznaOpole/posts/pfbid0TUpQBM72SqMLJXzRo4VMs8Zg4CpXLS27JpvQcwSVGoqYgV7hrWfDFyCckfGhUkxcl"
    target=_blank>Image source</a>.
  </em>
</p>

To be precise, the definition of the [*Nash Equilibrium*](https://www.britannica.com/science/Nash-equilibrium) reads the follows:

> A strategy profile, in which no player’s expected utility can be improved by changing one’s own strategy.

Nash's important contribution was to show that such an equilibrium always exists in any finite Game (i.e., games with a finite number of Players and finite Action sets), if Players can randomise their strategies (i.e., use mixed strategies).
(Although such an equilibrium strategy profile always exists, it might not be unique, i.e., the same Game can allow multiple collective behavioral patterns that can't be improved by individual deviations, therefore multiple strategy profiles can fulfill the condition for equilibrium.)

As it has been spelled out by Rubinstein in a previous quote, these equilibria can be interpreted as self-consistent beliefs of the Players about each other's strategies. (In other applications of Game Theory - such as in biology - repeated interactions can have very real effects on the Players' local environments, therefore the equilibria can be alternatively interpreted as a fixed point of an adaptive co-learning or co-evolutionary process through interactive interactions.)

## Decision Theory and Uncertainty

<p align="center">
  <img src="img/DALLEMetaPhysicsResearch.webp" alt="MetaPhysics Research Lab" width="500">
</p>
<p align="center">
  <em>
    Generated image by DALL·E to the prompt: "Metaphysics Research Lab" (February 2024).
  </em>
</p>

> Every day, in our professional work and our personal lives, each of us must make a multitude of decisions, both major and minor, under various conditions of uncertainty and partial ignorance.

This quote is from the [Encyclopedia of Statistical Sciences](https://onlinelibrary.wiley.com/doi/book/10.1002/0471667196) and highlights the importance and practical unavoidability of decision-making under uncertainty.
The general approach that I will describe in the following could be characterized as a form of "Bettabilitarianism":

> The universe is a mystery. We can never know anything for certain; we can only place bets one way or another. Like any gambler, however, we should gather as much information as possible before wagering our money or our lives.
Only then can we be confident in the bets we have made.

However, I aim to equip the reader with decision-making tools that can suggest reasonable actions even if we possess only a finite amount of relevant data.
(The quote is attributed to Oliver Wendell Holmes Jr. and can be found in the book [The Great Dissent](https://www.alumni.columbia.edu/content/great-dissent-how-oliver-wendell-holmes-changed-his-mind-and-changed-history-free-speech).)

### Uncertainty

By *uncertainty* I mean "known possibilities with unknown probabilities", i.e. the concept of states, parameters, or variables to which we can associate possible values but for which we cannot assign credible probabilities. In naming, I will follow Frank Knight's seminal book from 1921: [Risk, uncertainty and profit](https://archive.org/details/riskuncertaintyp00knigrich/page/n5/mode/2up), in which Knight distinguishes Risk (where we can talk about probabilities) and [Uncertainty](https://en.wikipedia.org/wiki/Knightian_uncertainty) (where not even the probabilities are known). I can suggest [Uncertainty in Economics](http://dx.doi.org/10.1007/978-3-319-55351-1) for a more up-to-date summary by Julia Köhn. (See a preview on [Google Books](https://books.google.co.uk/books?id=AA4rDwAAQBAJ&printsec=frontcover&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false).)
In the literature, uncertainty is often referred to as ambiguity as well.

To show what John Maynard Keynes was uncertain about [in 1937](https://discovery.ucl.ac.uk/id/eprint/16387/1/16387.pdf), I would like to quote his words [directly](https://www.jstor.org/stable/1882087):

> By 'uncertain' knowledge, let me explain, I do not mean merely to distinguish what is known for certain from what is only probable. The game of roulette is not subject, in this sense, to uncertainty; nor is the prospect of a Victory bond being drawn. Or, again, the expectation of life is only slightly uncertain. Even the weather is only moderately uncertain. The sense in which I am using the term is that in which the prospect of a European war is uncertain, or the price of copper and the rate of interest twenty years hence, or the obsolescence of a new invention, or the position of private wealth owners in the social system in 1970. About these matters there is no scientific basis on which to form any calculable probability whatever. We simply do not know. 

In my experience, the ordinary, everyday meaning of uncertainty is clear and intuitive for people who are not theorising but need to live and function in the real world. 


<p align="center">
  <img src="img/Wanderer.jpeg" alt="Wanderer above the Sea of Fog" height="450">
</p>
<p align="center">
  <em>
    <em>Wanderer above the Sea of Fog</em> (Der Wanderer über dem Nebelmeer) by Caspar David Friedrich. Original image from 
    <a href="https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Wanderer_above_the_Sea_of_Fog.jpeg"
    target=_blank>Wikimedia</a>.
  </em>
</p>

However, the concept becomes harder to define as we attempt to formalise it, because it slips from the grasp of mainstream theories and frameworks.
(I think this lack of formal language is an important reason why uncertainty fell out of the economic and scientific mainstream, relative to the 1920s and 1930s.)
Some executives, managers, and decision-makers might question why bother formalising something that resists theory, if we have good-enough intuition and heuristics to deal with it in practice?
My answer to this is that, of course, formalisation should not replace common sense, but it does make refinement, generalisation, and scaling feasible. (This is especially important in the age of Big Data and AI, where one who can automate and scale sensible decision-making can gain a significant advantage.)

### Navigating Uncertainty

>  I do not think I know what I do not know // ὅτι ἃ μὴ οἶδα οὐδὲ οἴομαι εἰδέναι 
-- **Socrates** (attributed by Plato in the [*Apology*](https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0169%3Atext%3DApol.%3Asection%3D21d), translated by [G. M. A. Grube](https://www2.hawaii.edu/~freeman/courses/phil100/04.%20Apology.pdf)) 399–360 BCE

> If you know what you know and know what you don't know that is true knowledge //
 知之为知之，不知为不知，是知也
-- Ancient Chinese saying attributed to **Confucius**, [*Analects [2.17]*](http://www.acmuller.net/con-dao/analects.html) (Paraphrased translation by [C. N. Yang](https://billmoyers.com/content/chen-ning-yang/)) 551–221 BCE




We used a negative definition for uncertainty, a variable that can take some values, but we have no credible probability distribution that could characterise these possible values.
This might be a valid definition, but to manage or make decisions in the face of uncertainty, it seems unavoidable to impose some structure on these variables or draw analogies with more familiar situations.

Contemplating the nature of uncertainties is, I think, almost by definition a metaphysical endeavour (this explains the cover image for this section). This does not mean, however, that these problems are completely untractable, only that different frameworks can be judged primarily by their consequences manifesting in the Agents' behaviour (and not by collecting empirical data to support or refute the assumptions of the framework in the real world).

Choosing the appropriate criteria for behaviour and judging its desirability is a delicate matter and may need to remain subjective. Still, I aim to show that some consequences of different metaphysical constructions can be determined and to reason for and against strategies in a principled way.

### Decision-making and Game Theory

In some sense, a Decision-making problem contains half of the information that a Game-theoretic framework would require: the decision maker knows her possible actions, has a model about possible "states of the world", and knows her own preferences. What is missing from a definition of a Game is the invention of an *other player* and setting its preferences.

Of course, assuming that the world is animated by a "strategic" *other player* and that it has preferences, is fictional and meant to be an analogy.
The usefulness of this metaphysical claim does not depend primarily on the forces and constituents of Nature (these influence only the known parts of our model), but it can be judged based on the policies it suggests for the decision-maker.
(Such claims can be judged by the fruits they bear - to paraphrase the popular wisdom - i.e. by the success of agents or communities adopting this framework.)

In a nutshell, the Game-theoretic framework for Decision-making under uncertainty suggests the following structure:

- If we can make the following modelling assumptions:
    - 0.) ⋆ There is an "Agent" who is part of the "World". The Agent can see only part of the World. Still, she can develop heuristics and, most importantly, perform actions;
    - 1.) The Agent considers only a finite number of possible Actions. (This set of Actions will be denoted by $\mathcal{A}$);
    - 2.) The Agent can (or is willing to) restrict the possible states of the world to a finite set. We will denote this set by $\Theta$ and call it the parameter set;
    - 3.) Lastly, the Agent can associate utilities (or rewards) to all potential consequences, which depend both on her action and the state of the world constituting a utility matrix (representable with a table).
- then the game-theoretic framework suggests the following:
    - I.) Imagine that the unknown parameter (or the state of the world) has been chosen by an opponent whose utility function is the regret of the Agent;
    - II.) Determine the optimal or equilibrium strategy for this fictional Game (this can be represented by a pair of potentially random strategies $( \sigma^* ,\pi^* )$, and Game Theory can be helpful to formally derive them.);
    - III.) Adopt the - potentially random - equilibrium strategy ($\sigma^∗$) of this imagined Game to choose an Action from the Action set ($\mathcal{A}$).

Loosely, this can be interpreted as introducing an imaginary "Trickster" Player behind the veil of uncertainty, whose only aim is to maximise the Agent's regret. Half-jokingly, this is a formalization of the well-known [Murphy's law(s)](https://www.eit.edu.au/the-truth-behind-murphys-law/): "If anything can go wrong, it will" [...] "and at the worst possible time, in the worst possible way".
Another often listed relevant [Murphy's general law](https://www.cs.cmu.edu/~fgandon/miscellaneous/murphy/) being: "Nature always sides with the hidden flaw".

However, before painting too pessimistic a picture, I need to highlight two things about this framework:

- It assumes that we are not defenseless against the "Trickster". Even if we think that there will be rain if we don't carry an umbrella and clear skies if we do, we assume that by randomising our choice, we can protect ourselves to some extent against always suffering the worst outcomes. In other words, we don't project mind-reading abilities to the "Trickster", only the aim of being our adversary. In this way, unpredictability can be utilised on the Agent's side, just as in Matching Pennies or Rock-Paper-Scissors.
- Another important clarification is that we don't assume that the "Trickster" is a totally malevolent Demon i.e. we are not projecting a strictly zero-sum game to the uncertain situation. (A zero-sum construction was the initial approach of [Abraham Wald](https://en.wikipedia.org/wiki/Abraham_Wald) in his work on [Statistical decision functions](https://catalog.hathitrust.org/Record/000469182), but it proved to be too pessimistic and lacks adaptivity in some realistic cases.)
The "Trickster" is assumed to care about our *regret* - the difference between the utility of the best possible action in hindsight and the action we actually took - and not about our total loss. (This important modification was made by [L. J. Savage](https://en.wikipedia.org/wiki/Leonard_Jimmie_Savage) in his influential book: The Foundations of Statistics.)
Keeping the Agent's expected utility maximizing aim, but assuming that the "Trickster" is focusing on regret instead of total loss, can be viewed as a built-in fear of missing out mechanism. We can reason that this "motivates" the "Trickster" to offer states that contain opportunities (because always offering only the worst case would be bad for us, but we could avoid feeling any regret). Therefore, this seemingly small change about the incentives of the imaginary adversary ultimately introduces hope and induces an explorative and much more adaptive mindset for the Agent. Turning pessimism to pragmatism.

<p align="center">
  <img src="img/RegretGhost.png" alt="Dusty purple ghost figurine" width="49%">
  <img src="img/RegretGhosts.png" alt="Group of ghost figurines" width="49%">
</p>
<p align="center">
  <em>
    Ghost figurines symbolising the regret-maximising “Trickster”. Original image source:
    <a href="https://www.yorkghostmerchants.com/original-york-ghost/project-one-z2fga-7yhl2-njr7m-6j5fm-74j42-t7w6n" target="_blank">Dusty Purple Ghost</a>
    by York Ghost Merchants (slightly colourised to match the colour coding used in the paper).
  </em>
</p>

A natural question arises if we want to generalize the concept for multiple Agents: whose regret the "Trickster(s)" ought to care about?

A part of the play [Copenhagen](https://en.wikipedia.org/wiki/Copenhagen_(play)) by Michael Frayn seems relevant to this question:

> **Bohr**:  It works, yes. But it’s more important than that. Because you see what we did in those three years, Heisenberg? Not to exaggerate, but we turned the world inside out! Yes, listen, now it comes, now it comes ... We put man back at the centre of the universe. Throughout history we keep finding ourselves displaced. We keep exiling ourselves to the periphery of things. First we turn ourselves into a mere adjunct of God’s unknowable purposes, tiny figures kneeling in the great cathedral of creation. And no sooner have we recovered ourselves in the Renaissance, no sooner has man become, as Protagoras proclaimed him, the measure of all things, than we're pushed aside again by the products of our own reasoning! We're dwarfed again as physicists build the great new cathedrals for us to wonder at the laws of classical mechanics that predate us from the beginning of eternity, that will survive us to eternity's end, that exist whether we exist or not. Until we come to the beginning of the twentieth century, and we’re suddenly forced to rise from our knees again.

> **Heisenberg**:  It starts with Einstein.

> **Bohr**: It starts with Einstein. He shows that measurement—measurement, on which the whole possibility of science depends—measurement is not an impersonal event that occurs with impartial universality. It’s a human act, carried out from a specific point of view in time and space, from the one particular viewpoint of a possible observer. Then, here in Copenhagen in those three years in the mid-twenties we discover that there is no precisely determinable objective universe. That the universe exists only as a series of approximations. Only within the limits determined by our relationship with it. Only through the understanding lodged inside the human head.

> **Margrethe**:  So this man you’ve put at the centre of the universe—is it you, or is it Heisenberg?

I have to add that I found no indication that Niels Bohr ever expressed such views in real life. Still, for any human (or Agent) centric framework, Margrethe's question in the play is spot on: Whose knowledge, preferences, and wishes are relevant? In our case, whose hopes and wishes, fears and doubts are imagined to guide the "Trickster(s)" activities behind the veil of uncertainty?

A relatively straightforward path to generalization to multiple Agents interacting in an uncertain environment is to assume that all Agents or Players are projecting their own "Trickster" to the uncertain parameters. (This explains the multiple ghost figurines on the right of the illustrative image above.)
This direction is explored in a separate, shorter arXiv paper: [Non-Cooperative Games with Uncertainty](https://arxiv.org/abs/2503.01889), where the concept of a so-called Extended Equilibrium is properly defined and, among other properties, its Existence is proven. (Under similar conditions that are sufficient for the existence of the traditional Nash equilibrium). 
The symphony of individual "Trickster" projection can be just as colorful and varied as this [ghost group photo](https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2d/fc/fd/bc/caption.jpg).
(For further resources on this topic, see the paper's [GitHub page](https://github.com/Konczer/UncertaintyTheory/tree/main/ExtendedEqilibrium).)

However, to stick to the original promise, I now return to the original topic - Statistical Games - in this blog post.

## Statistical Games

Compared to the introduction the paper in question is much less philosophical. This might be a disappointment for some who become interested in the topics discussed so far. However for the less philosophically inclined readers it might be a relief that the content and the results of the paper can be understood and appreciated without delving into murky metaphysical speculations and details about interpretations.

For those who are interested in the "philosophical why" beyound this informal introduction I suggest to take a look to this separate document: [Essay on Uncertainty](https://raw.githubusercontent.com/Konczer/UncertaintyTheory/refs/heads/main/Essay/pdf/EssayOnUncertainty.pdf).

<p align="center">
  <img src="img/StatisticalGames.png" alt="Statistical Games figure" width="400">
</p>
<p align="center">
  <em>
    (Figure 6 in
    <a href="https://arxiv.org/abs/2402.15892" target="_blank">arXiv:2402.15892</a>.)
  </em>
</p>

### Aim of the paper

In the first part of the paper, I simply posed a problem entirely in the framework of traditional Game Theory: Two players are playing a choosing-guessing game. 
This is a somewhat cautious approach to model building, in which I investigated the behaviour of a construction in a well-established framework, explored formally its various limiting cases and generalisations, resulting in rigorous standalone mathematical statements.
Mathematical theorems have the virtue that they stay valid under various interpretations - ["The same equations have the same solutions"](https://www.physics.udel.edu/~watson/phys208/quotes/quote11.html) -, therefore the formal results from this paper can be later used as supporting arguments for a completely Game-theoretical framework for statistics and maybe even probability theory.
(However, for those who are not interested in such reinterpretation, the Game-theoretical results of the paper can still remain interesting, which was the main reason for separating the mathematical and philosophical parts of the work into supporting but separate branches of the same project.)

In these games, Players do not choose and guess blindly. The chooser (Player 2) needs to produce a finite binary sequence with a given amount of $1$-s and $0$-s, while the guesser (Player 1) can sample a portion of the sequence and make her guess based on the collected sample.

In the paper, I intentionally chose the simplest possible construction in which statistical concepts can first emerge. This has a downside because the investigated problem can seem too simple for most real-world statistical problems. However, by investigating the simplest toy model, I was able to talk about statistical and probabilistic concepts without introducing any external stochastic (random) processes, and I was able to prove (or at least conjecture) rigorous results for various limiting cases and deformations of the construction.
Which is an important step in applying the correspondece principle i.e. identifying and matching the concepts of Game-theoretic guessing or betting Games with traditional statistical concepts.

Therefore, the main aim of the paper was to investigate a simple toy model in Game Theory and use it as a proof of concept for using the framework to handle decision-making problems involving uncertainty.

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

