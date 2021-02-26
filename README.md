# Post-Correspondence-Solver
Command line application that solves the [Post Correspondence Problem](https://www.geeksforgeeks.org/post-correspondence-problem/) using the iterative deepening depth-first search algorithm.

## Usage
* Uncomment an input file (lines 120 to 124) to select from different problems.
  * Input file format:
    * Maximum queue length for breadth-first portion
    * Maximum number of nodes to expand
    * Verbose flag (prints node expansion if 1)
    * The number of dominoes in the set
    * The set of dominoes (one line per domino)
    
* Run the solver:   ```python3 pc_solver.py```
