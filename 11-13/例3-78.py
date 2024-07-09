import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1651256989)
dataset = np.random.normal(size=(500,1))
# 绘制垂直的小提琴图
parts = plt.violinplot(dataset,
                       quantiles=[0.2,0.4,0.6,0.8])
# 设置分位数线条颜色
parts['cquantiles'].set_colors(['r','g','b','k'])
plt.show()
