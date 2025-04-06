**Flappy Bird with AI (NEAT)**

This repository contains a Flappy Bird clone implemented in Python with AI, using the NEAT (NeuroEvolution of Augmenting Topologies) algorithm to solve the game. The AI learns to play the game through multiple simulations, evolving its neural network over generations.

**Features**

Flappy Bird Game: A Python implementation of the classic Flappy Bird game.

NEAT AI: The game is solved using the NEAT algorithm, which evolves neural networks to maximize performance in the game.

Multiple Simulations: The AI runs through multiple simulations to improve and adapt, enhancing its ability to play the game.

Visualization: Visual representation of the game and the neural network training process.

**Requirements**

Python 3.x

Pygame

NEAT-Python

**How NEAT Works**

The NEAT algorithm evolves a population of neural networks over generations. Each neural network controls the movement of the bird in the game. Initially, the neural networks are random, and through the process of selection, crossover, and mutation, the networks are refined over generations, eventually learning how to play the game optimally.

Selection: The best-performing neural networks are selected to reproduce.

Crossover: Neural networks from the previous generation are crossed over to create new networks.

Mutation: Random changes are applied to the neural networks, introducing new possibilities for behavior.

**License**

This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgements**

Flappy Bird: Original game created by Dong Nguyen.

NEAT: NeuroEvolution of Augmenting Topologies developed by Kenneth O. Stanley.

