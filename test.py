from interpolation import LinearInterpolation
from interpolation import QuadraticInterpolation
from scipy.interpolate import lagrange
import numpy as np

# Test Linear Interpolation
pontos = [(60, 2700), (70, 3000)]
g = 62
nPontos = 2

linearIp = LinearInterpolation(pontos)
print(linearIp.P(g))  # 2760.0000000000005

# Test Quadratic Interpolation
pontos = [(3, 20.08), (3.2, 24.53), (3.4, 29.96)]
g = 3.1
nPontos = 3
quadIp = QuadraticInterpolation(pontos)
print(quadIp.P(g))  # 22.18249999999999
# 12.250000000000622 * x ** 2 + -53.70000000000398 * 2 + 70.93000000000636
print(quadIp.getP())

# Test Lagrange Interpolation
x = np.array([1, 3, 4])
y = x**3
print(lagrange(x, y))
