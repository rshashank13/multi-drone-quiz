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

**Note:** the algorithm in the paper returns squared euclidean distances, and we need to finally take a square_root of it.  

Overall complexity - $O(dk)$ where $d = 2$, $k = M * N$

##### Result:
Time taken for 2e4 computations for both matrices: 11.537185907363892

---
#### Question 2:
We have N drones and M obstacles. For each drone, we need to calculate the distance to the nearest obstacle. Obstacles are static while drones are dynamic, i.e. they change their positions at discrete timesteps. 

For each drone, every time it moves, how can we compute its distance to the closest obstacle? Is it possible to do it without a brute-force approach?

##### Solution:
We can solve this using the above ESDF algorithm,
1. We will first create a map of some arbitrary dimensions (say X, Y) such that all the obstacles appear within the X x Y map. 
2. We will compute the ESDF map for the above X x Y map. Now we have distances to closest obstacle from each $(i,j)$ where $i$ in $[0,X]$, $j$ in $[0,Y]$
3. For each drone $d$, we can now simply lookup the distance to the closest obstacle. Computing distance to nearest obstacle for a given drone at timestep $t$ is same as $Df(i, j)$ where $(i,j)$ is the position of the drone $d$ at timestep $t$.

---
#### Question 3:
Based on Problem #2, what if we want to calculate the distances to K nearest obstacles? Can you propose an efficient algorithm for this?

##### Solution:
method - 1: Similar to the above solution, we can compute the 1st nearest obstacle for a grid point $(i, j)$, and next we remove that closest obstacle and compute the nearest obstacle again, and we do this k-times

method - 2: we modify the ESDF algorithm now to keep track of k lower envelopes at each point (using a max/min-heap) and then we compute the distance Df(p) for each of the k lower envelopes.
