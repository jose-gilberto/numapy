import numpy as np


class MultipleLinearFitting:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x[0]) + 1

    def solve(self):
        A = np.zeros((self.n, self.n))
        A[0][0] = n
        print(A)