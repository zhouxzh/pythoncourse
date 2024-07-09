import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1651597276)
n = 100000
x = np.random.standard_normal(n)
y = np.random.standard_normal(n)
xmin, xmax = x.min()-0.5, x.max()+0.5
ymin, ymax = y.min()-0.5, y.max()+0.5

# 创建3个水平子图，共享y轴，只有左边第一个显示y轴刻度
fig, axs = plt.subplots(ncols=3, sharey=True)
# 调整子图之间的水平距离
fig.subplots_adjust(wspace=0.2)
# 绘制散点图，密集处相邻的散点会互相交叉和重叠，无法看清
axs[0].scatter(x, y)
axs[0].axis([xmin, xmax, ymin, ymax])
axs[0].set_title('scatter')
axs[0].set_aspect('equal')

# 绘制二维直方图，使用六边形表示每个散点，密集处颜色叠加
# 颜色越明亮，说明该位置散点重叠的数量越多
hb = axs[1].hexbin(x, y, gridsize=50, cmap='inferno')
axs[1].axis([xmin, xmax, ymin, ymax])
axs[1].set_title('Hexagon binning')
axs[1].set_aspect('equal')
# 颜色条属性，颜色条标签属性
cb_prop = dict(orientation='vertical', fraction=0.046, pad=0.01)
cbl_prop = dict(fontsize=8, weight='bold', labelpad=0)
fig.colorbar(hb, ax=axs[1], **cb_prop).set_label('counts', **cbl_prop)

# 绘制二维直方图，对颜色值取对数
hb = axs[2].hexbin(x, y, gridsize=50, bins='log', cmap='inferno')
axs[2].axis([xmin, xmax, ymin, ymax])
axs[2].set_title('With a log color scale')
axs[2].set_aspect('equal')
fig.colorbar(hb, ax=axs[2], **cb_prop).set_label('log10(N)', **cbl_prop)

plt.show()
