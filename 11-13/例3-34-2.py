import numpy as np
import matplotlib.pyplot as plt

X = [list(range(0,10,2)), list(range(3,16,3))] * 3
Y = [[0]*5, [1]*5, [2]*5, [3]*5, [4]*5, [5]*5]
np.random.seed(1651370849)
C = np.random.random((len(X), len(Y[0])))
# 渐变色填充
plt.pcolormesh(X, Y, C, shading='gouraud',
               edgecolors='b', alpha=0.7)
plt.gca().set_aspect('equal')
plt.show()
