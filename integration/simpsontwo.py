import numpy as np


class SecondSimpsonIntegration:

    def __init__(self, k, a, b):
        self.k = k
        self.a = a
        self.b = b
        self.h = (b - a)/k
        self.solve()

    def f(self, x):
        return np.log(x)/x**2

    def solve(self):
        calculus = self.f(self.a) + self.f(self.b)
        for i in range(self.k):
            if i % 3 == 0:
                calculus += 2 * self.f(self.a + i * self.h)
            else:
                calculus += 3 * self.f(self.a + i * self.h)

        calculus = (3*self.h)/8 * calculus
        print(calculus)
