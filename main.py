import time
from result import *
import numpy as np


def compute_matrix(M, N, obstacle_list):
    X = np.zeros((M, N))
    for obstacle in obstacle_list:
        i,j = obstacle
        X[i][j] = 1
    return X

def l2_1D(X, is_indicator):
    f = X.copy()
    if is_indicator:
        f[f==0] = 1e10
        f[f==1] = 0
    
    k = 0 # Index of rightmost parabola in lower envelope
    v = np.zeros_like(f).astype(np.int16) # Locations of parabolas in lower envelope 
    z = np.zeros(len(f) + 1) # location of boundaries between parabolas
    z[0] = -np.inf
    z[1] = np.inf
    flag = 0

    for q in range(1, len(f)): # Compute lower envelope
        flag = 0
        while(flag != 1):
            s = ((f[q] + q**2) - (f[v[k]] + v[k]**2)) / (2*q - 2*v[k])
            if s <= z[k]:
                k = k - 1
                flag = 0 #goto 6
            else:
                k = k + 1
                v[k] = q
                z[k] = s
                z[k+1] = np.inf
                flag = 1 #goto next q

    k = 0
    d = []
    for q in range(len(f)): # Fill in values of distance transform
        while z[k+1] < q:
            k = k + 1
        d.append((q - v[k])**2 + f[v[k]])
    d = np.array(d)
    return d


def esdf(M, N, obstacle_list):
    """
    :param M: Row number
    :param N: Column number
    :param obstacle_list: Obstacle list
    :return: An array. The value of each cell means the closest distance to the obstacle
    """
    matrix = compute_matrix(M, N, obstacle_list)
    for x in range(M):
        row = matrix[x, :]
        matrix[x, :] = l2_1D(row, is_indicator=True)
    
    for y in  range(N):
        column = matrix[:, y]
        matrix[:, y] = l2_1D(column, is_indicator=False)
    
    matrix = np.sqrt(matrix)
    return matrix


if __name__ == '__main__':
    st = time.time()
    for _ in range(int(2e4)):
        assert np.array_equal(esdf(M=3, N=3, obstacle_list=[[0, 1], [2, 2]]), res_1)
        assert np.array_equal(esdf(M=4, N=5, obstacle_list=[[0, 1], [2, 2], [3, 1]]), res_2)

    et = time.time()
    print(et-st)
