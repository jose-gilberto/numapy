import numpy as np


class Trapeze:

    def __init__(self, t, n, a, b):
        self.a = a
        self.b = b
        self.n = n
        self.t = t
        self.h = (b-a)/n
        self.solve()

    def f(self, x):
        return np.e ** (-x**2/2)

    def solve(self):
        if self.t == 'compost':
            self._solveCompost()
            return

    def _solveCompost(self):
        som = self.f(self.a) + self.f(self.b)
        sum_h = self.h + self.a
        for i in range(self.n - 1):
            som += 2 * self.f(sum_h)
            sum_h += self.h

        calculus = self.h/2 * som
        print(calculus)

        