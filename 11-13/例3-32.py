import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt

# 顶点坐标
points = np.array([[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0],
                   [-1, -1], [0, -1], [1, -1], [0, 0]])
# 三角形网格的顶点编号
triangles = np.array([[8, 0, 1], [8, 1, 2], [8, 2, 3], [8, 3, 4],
                      [8, 4, 5], [8, 5, 6], [8, 6, 7], [8, 7, 0]])

np.random.seed(1651139976)
# 顶点颜色
colors = np.random.random(len(points))
# 绘制三角形网格，使用位置参数colors设置所有顶点的颜色
# 三角形内部和边线颜色根据顶点颜色进行插值计算
# 使用facecolors=colors可以指定每个三角形的颜色，此时colors长度应与三角形数量相等
# shading='flat'时使用单色填充三角形内部，shading='gouraud'时插值计算三角形内部颜色
plt.tripcolor(points[:,0], points[:,1], triangles, colors,
              shading='gouraud')
plt.show()
