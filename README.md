# Multi-drone-quiz

#### Question 1:
We have a MxN grid. In the grid, some cells are occupied with obstacles. Your task is to compute a grid in which each cell stores its closest distance to the nearest obstacle.

For example, there is a 3x3 grid below, and the two cells filled with green color means these two cells are obstacles. Obstacle indices are [0,1] and [2,2], where the first component is the row (x-index) and the second component is the column (y-index).

```
Input: M=3, N=3, obstacle_list=[[0, 1], [2, 2]]
Output: [[1.0, 0.0, 1.0], 
   [sqrt(2), 1.0, 1.0], 
   [2.0, 1.0, 0.0]]
```
#### Solution:

Code - in main.py
required libraries - numpy

##### Method: 
I have used the algorithm proposed in the paper "[Distance Transforms of Sampled Functions](http://people.cs.uchicago.edu/~pff/papers/dt.pdf)".

In 1D - The algorithm for computing this distance transform has two distinct steps. First we compute the lower envelope of the n parabolas (1D). We then fill in the values of Df (p) by checking the height of the lower envelope at each grid location p.

In 2D - The same algorithm as above is applied twice - once for rows, and then for columns

##### Result:
Time taken for 2e4 computations for both matrices: 11.537185907363892
