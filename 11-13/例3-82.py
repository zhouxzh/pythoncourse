import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1652135199)
# 倒钩的位置
X, Y = np.mgrid[-1.2:1.2:5j, -1.2:1.2:5j]
U = np.random.randint(-45, 45, (len(X),len(X[0])))
V = np.random.randint(-45, 45, (len(Y),len(Y[0])))
bb = plt.barbs(X, Y, U, V, np.random.random((len(X),len(Y))))
plt.colorbar(bb)
plt.xlim(-1.6, 1.6)
plt.ylim(-1.6, 1.6)

# 设置纵横比相等
plt.gca().set_aspect('equal')
plt.show()