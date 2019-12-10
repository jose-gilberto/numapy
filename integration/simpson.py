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
        x = []
        fx = []

        i = 0
        while i <= self._k:
            x.append(self._a + i * self.h)
            fx.append(self.f(x[i]))
            i += 1

        res = 0
        i = 0
        while i <= self._k:
            if i == 0 or i == self._k:
                res += fx[i]
            elif i % 2 != 0:
                res += 4 * fx[i]
            else:
                res += 2 * fx[i]
            i += 1
        res = res * (self.h / 3)
        print('O resultado da integração numérica é: {}'.format(res))
