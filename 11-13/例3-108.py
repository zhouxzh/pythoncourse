import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,np.pi*4, 0.01)
y = np.sin(x)

plt.plot(x, y)
plt.ylabel('sin\n正\n弦\n值',         # 坐标轴文本标签
           fontproperties='simsun',   # 中文字体
           rotation='horizontal',     # 文本方向，还可以为vertical
           fontsize=12,               # 字号
           va='bottom',               # 设置垂直居下，还可以为top或center
           ha='left',                 # 水平居左
           labelpad=15,               # 文本与坐标轴之间的距离
           linespacing=2,             # 行距，单位为points
           position=(-10,0.3))        # 垂直方向的位置，可以忽略第一个数
plt.xlabel('自变量', fontproperties='simhei', fontsize=12)
plt.title('正弦图像', fontproperties='simhei', fontsize=16)

plt.show()
