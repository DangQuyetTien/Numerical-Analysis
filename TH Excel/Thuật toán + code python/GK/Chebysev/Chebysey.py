import numpy as np
def hamSo(x):
    return x**2*np.exp(-2*x**2) + 3 * np.cos(x)**2 - 5*np.exp(x)

# n bậc của đa thức => có n + 1 mốc
def cacMocToiUu(n, a, b):
    x = []
    for i in range(n + 1):
        x.append(1/2 *((b - a) * np.cos((2*i + 1)*np.pi/(2 * n)) + a + b))
    return [np.array(x), hamSo(np.array(x))]


a = 1
b = 5
n = 9

listMoc = cacMocToiUu(n, a, b)
print("x: {0}\ny: {1}".format(listMoc[0], listMoc[1]))