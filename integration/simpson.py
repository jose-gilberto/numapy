import numpy as np


class SimpsonIntegration:

    def __init__(self, func, k, a, b):
        self.f = func
        self._k = k
        self._a = a
        self._b = b
        self.h = (b - a)/k
        self.solve()

    def solve(self):
        calculus = self.f(self._a) + self.f(self._b)

        for i in range(self._k):
            if i % 2 == 0:
                calculus += 4 * self.f(self._a + i * self.h)
            else:
                calculus += 2 * self.f(self._a + i * self.h)

        calculus = self.h/3 * calculus
        print(calculus)


