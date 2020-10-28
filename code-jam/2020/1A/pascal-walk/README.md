# Pascal Walk

- [solution.py](solution.py) solves two test sets, but not the third (Wrong Answer)
- [gotta_go_fast.py](gotta_go_fast.py) solves all three test sets using recursion
- [another_gotta_go_fast.py](another_gotta_go_fast.py) solves all three test sets using an iterative approach
- [binary_representation.py](binary_represetation.py) solves all three test sets

## Gotta Go Fast

Get to the higher values as soon as possible by zig-zagging down through the middle of Pascal's triangle.
Stop when going at the lower level would force the sum to exceed the target.
Move to the left or down till the target is met, as before avoid moving down when that choise would exceed the taget.

## Binary Represetation

Each level of the Pascal's triangle sums up to 2^i where i is the "depth" of the level (starting from 0).
With this information in mind it is possible to break down the target in its binary format and path through those level
corresponding to a 1 in the binary decomposition and "skip" those with a 0.

