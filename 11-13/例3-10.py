import numpy as np
import matplotlib.pyplot as plt

x = [1, 3, 5, 8, 9]
y = [5, 9, 3, 5, 10]
plt.errorbar(x, y,    # 数据点位置
             xerr=1, yerr=[1,1,1,0.5,0.5],    # 两个方向的误差范围
             # 设置线条和端点符号
             # fmt='none'时表示不绘制数据点及连线，只绘制误差标记
             fmt='-.*',
             ecolor='orange',    # 误差线颜色
             errorevery=2,       # 每2个数据点绘制一个误差线
             lolims=True,        # 只绘制上侧的误差线
             xlolims=True,       # 只绘制右侧的误差线
             )

plt.show()
