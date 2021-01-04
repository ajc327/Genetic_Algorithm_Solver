==========================
genetic_algo

===========================

## Overview

This package contains code for a genetic algorithm solver. This algorithm simulates the process of natural evolution,
and works using the encoding of the control variables, rather than the variables themselves.

The algorithm search from one population of solutions to another, rather than from individual to individual.

The algorithm only requires the objective function information, and no derivative information is required.

Probabilistic, not deterministic, transition rules are used.


## Structure
The following steps are taken to arrive at an approximately best solution:
1. An initial population is generated in the input space.
2. The initial Population is assessed.
3. The parents are selected.
4. A new population is bred using crossover.
5. The new population undergoes probabilistic mutation
6. The new population is assessed
7. The archives are updated.
8. The search is terminated if the maximum number of generation is reached.

## Solution representation
The solutions are represented by binary bit strings. For integers this can be easily done. For continuous variables,
they are quantised and approximated.


## Parent selection
- The initial population is selected randomly.
- Ranking based selection is used to calculate the probability of selection for a particular individual based on their
fitness.
- Stochastic remainder selection without replacement is used to remove some variance from the selection process.
    - In this process the expected copies of each solution is calculated and the fractional remainder of taking the floor is used for further selection.

The code is modular. It is easy to implement another type of parent selector which satisfies the interface.
The input is a list of Member objects, and the output needs to be a pool of candidates.

## Recombination
- 1 point crossover on the reduced surrogates on the binary encoding is used to enable recombination.
- The process occurs probabilistically with the probability controlled by the parameter p_cross

Again, this was implemented in a modular way. To implement another crossover strategy, additional crossover functions can be added into ga_crossover.
This has an easy interface, it takes the binary encoding of the parents and outputs the binary encoding of the two offspring.

## Mutation
This is very much a background operator, as it is in nature. The purpose is to provide insureance against the irrevocable loss of genetic information.
As such, diversity within the population is maintained.

In traditional GA, every bit of every solution is potentially susceptible to mutation.

Each bit is subjected to a simulated weighted coin toss with a probability of mutation Pm.

=====================================

## Example usage:

'''
from genetic_algo import *
solver = GASolver(funcrana, n_dim=2, population_size=100, )
best_solutions = solver.run()

'''