#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
n0 = 1000
n1 = 1000
x0 = np.linspace(-2, 2, n0)
x1 = np.linspace(-2, 4, n1)
(X0, X1) = np.meshgrid(x0, x1)
Z = X0 ** 4 / 3 + X1 ** 2 / 2 - X0 * X1 + X0 - X1

# breaks  = np.linspace(-1, 1,  11)

plt.figure()
CS1 = plt.contour(x0, x1, Z, 150, colors='k')
plt.xlabel('angles  1')
plt.ylabel('angles  2')
plt.grid()
plt.title('sine  cosine  wave')
plt.show()

