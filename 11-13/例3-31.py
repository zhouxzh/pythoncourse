import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors

# 顶点坐标
points = np.array([[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0],
                   [-1, -1], [0, -1], [1, -1], [0, 0]])
# 三角形网格的顶点编号
triangles = np.array([[8, 0, 1], [8, 1, 2], [8, 2, 3], [8, 3, 4],
                      [8, 4, 5], [8, 5, 6], [8, 6, 7], [8, 7, 0]])

plt.triplot(points[:,0], points[:,1], triangles,
            marker='*', markersize=10,
            markerfacecolor='orange', markeredgecolor='red',
            color='blue', lw=0.5)
plt.show()
