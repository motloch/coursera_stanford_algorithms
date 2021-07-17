"""
Code of the Strassen's subcubic matrix multiplication algorithm

Based on the Week Two of the 'Divide and Conquer, Sorting and Searching, and Randomized
Algorithms' course on Coursera (Algorithms Specialization, Stanford University)
"""
import numpy as np #Use numpy arrays for convenience

def strassen(X, Y):
    """
    Implementation of Strassen's matrix multiplication algorithm

    Returns product X*Y of two n*n matrices X, Y (assumes numpy arrays)

    Assumes n is a power of two, for simplicity
    """

    #Check input
    assert(isinstance(X, np.ndarray)), 'First argument must be numpy array'
    assert(isinstance(Y, np.ndarray)), 'Second argument must be numpy array'
    assert(len(X.shape) == 2), 'First argument should have two dimensions'
    assert(len(Y.shape) == 2), 'Second argument should have two dimensions'
    n = X.shape[0]
    assert(X.shape[1] == n), 'First matrix should be rectangular'
    assert(Y.shape == (n, n)), 'The two matrices should have the same size'
    assert((n == 1) or (n % 2 == 0)), 'Assumes matrices of size 2^n'

    #Terminate the recursion
    if n == 1:
        return X*Y

    #Variable names as in the Coursera video
    A = X[:n//2, :n//2]
    B = X[:n//2, n//2:]
    C = X[n//2:, :n//2]
    D = X[n//2:, n//2:]
    E = Y[:n//2, :n//2]
    F = Y[:n//2, n//2:]
    G = Y[n//2:, :n//2]
    H = Y[n//2:, n//2:]

    P1 = strassen(A,   F-H)
    P2 = strassen(A+B, H)
    P3 = strassen(C+D, E)
    P4 = strassen(D,   G-E)
    P5 = strassen(A+D, E+H)
    P6 = strassen(B-D, G+H)
    P7 = strassen(A-C, E+F)

    result = np.zeros((n,n))

    result[:n//2, :n//2] = P5 + P4 - P2 + P6
    result[:n//2, n//2:] = P1 + P2
    result[n//2:, :n//2] = P3 + P4
    result[n//2:, n//2:] = P1 + P5 - P3 - P7

    return result

if __name__ == "__main__":
    #Test it out on a simple example
    A = np.array([
            [5, 6, 1, 4],
            [9, 6, 0, 4],
            [5, 3, 1, 2],
            [5, 6, 2, 4],
        ])
    B = np.array([
            [2, 6, 1, 4],
            [3, 0, 0, 1],
            [4, 2, 1, 2],
            [5, 1, 2, 4],
        ])
    #Exact results:
    AB = np.array([
            [52,36,14,44],
            [56,58,17,58],
            [33,34,10,33],
            [56,38,15,46],
        ])
    BA = np.array([
            [89,75,11,50],
            [20,24,5,16],
            [53,51,9,34],
            [64,66,15,44],
        ])

    assert(np.min(np.abs(strassen(A, B) - AB)) == 0)
    assert(np.min(np.abs(strassen(B, A) - BA)) == 0)
