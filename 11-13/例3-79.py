import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1651256989)
dataset = np.random.normal(size=(500,3))
parts = plt.violinplot(dataset,        # 每列数据一个图
                       vert=False,     # 水平方向
                       showmeans=True, # 显示均值
                       showextrema=True,  # 显示最值
                       showmedians=True,  # 显示中值
                       )
plt.yticks([1, 2, 3], list('ABC'))
# 最小值使用红色显示，也支持设置不同颜色，例如['r','g','b']
parts['cmins'].set_edgecolor('red')
# 最大值使用蓝色显示
parts['cmaxes'].set_edgecolor('blue')
# 均值使用橙色显示
parts['cmeans'].set_edgecolor('orange')
parts['cmeans'].set_linewidth(0.5)
# 中值使用绿色显示
parts['cmedians'].set_edgecolor('green')
parts['cmedians'].set_linewidth(0.5)
# 中间轴线的颜色
parts['cbars'].set_edgecolor('black')
# 设置小提琴图主体部分的填充色、填充符号、边线宽度、线形和颜色
parts['bodies'][0].set_facecolor('gray')
parts['bodies'][0].set_alpha(0.4)
parts['bodies'][0].set_hatch('o')
parts['bodies'][0].set_linewidth(2)
parts['bodies'][0].set_linestyle('--')
parts['bodies'][0].set_edgecolor('blue')

plt.show()
