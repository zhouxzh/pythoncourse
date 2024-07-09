import numpy as np
import matplotlib.pyplot as plt

k = 1                                          # 反比例函数xy=k的常数k
m, n = 6, 3                                    # 矩形右上角坐标(m,n)
x = np.arange(0.1, m+0.5, 0.02)                # 第一象限中反比例函数曲线上顶点的x坐标
y = k / x                                      # 根据反比例函数xy=k计算顶点y坐标
plt.plot(x, y, 'b')                            # 绘制第一象限指定区间内的反比例函数图像

plt.plot([0,m,m,0,0], [0,0,n,n,0], 'r')        # 绘制矩形，从左下角出发，向右、上、左、下
plt.plot([0,m], [n,0], 'g')                    # 矩形对角线
plt.plot([k/n,m], [n,k/m], 'g')                # 矩形与反比例函数的交点连线

for x, y, ch in zip([0,m,m,0,k/n,m], [0,0,n,n,n,k/m], 'OABCDE'):
    plt.text(x, y+0.02, ch)                    # 绘制顶点与交点的符号
plt.xlim(-0.1, m+1)                            # 设置坐标轴跨度
plt.ylim(-0.1, n+1)
plt.title(f'k={k},m={m},{n=}', fontsize=20)   # 设置图形标题
plt.gca().set_aspect(True)                     # 设置图形纵横比相等

plt.show()                                     # 显示图形
