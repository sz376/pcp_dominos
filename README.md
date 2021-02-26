# Post-Correspondence-Problem Dominoes Solver
The  POST  CORRESPONDENCE  PROBLEM  is  defined  as  follows:  You  are  given  a collection of dominoes.  Each domino has a string of characters on top and another string on the bottom.  (Both strings are non-empty.)  You can make as many copies of the dominoes as you need.  The problem is to place the dominoes side by side so that the combination of the strings on the top is the same as the combination of the strings on the bottom. A cleverer state space for this problem defines a ”state” to be either the part of bottom that goes past the top, or vice versa.  For example, if you have the dominoes D1=abb/ab, D2=a/baab, D3=ac/acab, then the two strings {D1,D2}=abba/abbaaband, {D3}=ac/acab can be considered the same state, because in either case you have to ”make up” a trailing ”ab” onthe bottom, and any sequence that can be added after{D1,D2}to solve the   work just as well when added after {D3}. In this program, the first stage of search, a breadth-first search is used through the state space detailed in the above until the queue of frontier states  has  reached  a  specified  maximum. In the second stage of search, iterative deepening is used starting from the frontier created in the first stage, until a specified limit has been reached.

## Usage
* Uncomment an input file to select from different inputs.
  * Input file format:
    * Maximum queue length for breadth-first portion
    * Maximum number of nodes to expand
    * Print sequence flag
    * The number of dominoes in the set
    * The set of dominoes (one line per domino)

* Run the solver:   ```python pcp_dominos.py```
