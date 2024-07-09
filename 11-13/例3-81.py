import numpy as np
import matplotlib.pyplot as plt

# 生成8个方向的角度
theta = np.linspace(0, 2*np.pi, 8, endpoint=False)
r = 1
# 每个风矢量的x、y位置
X = r * np.cos(theta)
Y = r * np.sin(theta)
np.random.seed(1652015794)
U = np.random.randint(1, 25, len(X))
V = np.random.randint(1, 25, len(X))
# 绘制风标图
plt.barbs(X, Y, U, V, np.random.random(len(X)))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

# 设置纵横比相等
plt.gca().set_aspect('equal')
plt.show()
