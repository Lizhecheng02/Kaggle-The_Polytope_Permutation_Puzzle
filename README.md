## This Repo is for [Kaggle - Santa 2023 - The Polytope Permutation Puzzle](https://www.kaggle.com/competitions/santa-2023)

### Task

In this competition, you will solve cube-like puzzles in the fewest moves, but instead of the usual cubes, the puzzles come in a variety of geometric shapes. 

### Cube Solution

- For lower-order Rubik's Cubes, a reinforcement learning algorithm, namely ``DeepCubeA``, can be used to solve them.

- For Rubik's Cubes of order four and above, reinforcement learning algorithms are not effective. Therefore, we need to use algorithms that imitate human methods of solving the Rubik's Cube (``rubiks-cube-NxNxN-solver``). However, the drawback of this approach is that the number of steps required will be much higher than the optimal solution.

### Wreath Solution

- For Wreath Rubik's Cubes of 33-order and below, we can use the ``DeepCubeA`` algorithm to solve them.

- For a 100-order wreath Rubik's Cube, it cannot be solved using reinforcement learning algorithms.

### Globe Solution

- No version of the globe Rubik's Cube has been solved using reinforcement learning, possibly due to the excessively large number of possible states for this type of cube, resulting in an extremely vast search space.

### Processing

- When we use the ``rubiks-cube-NxNxN-solver`` to solve the Rubik's Cube, we need to convert the input format provided by the competition into the input order required by the code. (This process is relatively complex, and this code has strict regulations on the arrangement of the Rubik's Cube input.)

- After obtaining the solution steps from the ``rubiks-cube-NxNxN-solver``, we need to convert them into the output format required for the competition, in accordance with the rotation labeling rules of the Rubik's Cube. (The conversion code is located in the main directory, where brute-force simulation can be used.)

### Code Modification

- Creating a new reinforcement learning environment.

- Switch the deep learning network from mlp to a convolutional neural network or a transformer structure.

- Change the network's input from a single initial state to two types of states: the initial state and the target state. This was originally intended to break down the process of solving the Rubik's Cube into many small steps and then continuously optimize these small steps. However, this was ultimately not successfully implemented.

### Conclusion

This competition has almost no relation to deep learning; the real solution is related to group theory in mathematics. The winning solution codes are almost all implemented in Rust or C.