from interpolation import LinearInterpolation
from interpolation import QuadraticInterpolation
from curvefitting import MultipleLinearFitting
from integration import Trapeze
from integration import SimpsonTwo
import numpy as np
from scipy import integrate

# Test Linear Interpolation
# pontos = [(30, 3), (40, 5)]
# g = 37
# nPontos = 2

# linearIp = LinearInterpolation(pontos)
# print(linearIp.P(g))  # 4.4

# Test Quadratic Interpolation
# pontos = [(3, 20.08), (3.2, 24.53), (3.4, 29.96)]
# g = 3.1
# nPontos = 3
# quadIp = QuadraticInterpolation(pontos)
# print(quadIp.P(g))  # 22.18249999999999
# 12.250000000000622 * x ** 2 + -53.70000000000398 * 2 + 70.93000000000636
# print(quadIp.getP())

# x = [[2, 3, 6, 4, 6],
#      [2, 3, 6, 4, 6],
#      [2, 3, 6, 4, 6],
#      [2, 3, 6, 4, 6]]
# y = [2, 3, 6, 5, 3]

# mp = MultipleLinearFitting(x, y)
# mp.solve()

# trapeze = Trapeze('compost', 10, -2, 2)
# simpson = SimpsonTwo(12, 0, 2)

# print(integrate.quad(lambda x: x**5, 0, 2)[0])
