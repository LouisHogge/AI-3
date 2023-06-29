# Introduction to Artificial Intelligence Project 3

## Project Description
In this third part of the project, Pacman got tired of ghosts wandering around him, so he bought a magic gun that make the ghosts edible. But while he shot them, he figured out that the gun also made them invisible. Fortunately, he also got his hands on a rusty distance sensor. The sensor returns a noisy Manhattan distance between pacman and each ghost, which Pacman can use as evidence to find the ghost positions. The noisy distance, denoted $e$, results from the addition of noise to the true Manhattan distance, the noise being sampled from a binomial distribution centered around 0.

$$ e = \text{ManhattanDistance}(\text{Pacman}, \text{Ghost}) + z - np \qquad z \sim \text{Binom}(n, p), $$

where $n=4$ and $p=0.5$.

Pacman knows that the ghosts are afraid of him and are more likely to take actions that makes it move away from him. Their exact action policy of the ghosts (afraid, fearless and terrified) should be deducted from the *ghostAgents.py* file.

Your task is to design an intelligent agent based on the Bayes filter algorithm (see Lecture 6) for locating and eating all the ghosts in the maze.
1. Implement the Bayes filter algorithm to compute Pacman's belief state of the ghost positions. To do so, fill in the three methods transition\_matrix, observation\_matrix and update of the BeliefStateAgent class. update must rely on transition\_matrix and observation\_matrix.
2. Implement a Pacman agent whose goal is to eat all the ghosts as fast as possible. However, at each step, the agent only has access to its own position and the current belief state of the ghost positions. To do so, fill in the _get_action method of the PacmanAgent class.

## How to Use the Project
For example, use the following command to run your Bayes filter implementation against a single afraid ghost in the large\_filter layout:
```bash
python run.py --ghost afraid --nghosts 1 --layout large_filter --seed 42
```
