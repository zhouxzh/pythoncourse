import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1651544461)
data = np.random.randint(1, 10, 300)
# 加参数histtype='step'可以绘制不填充的阶梯图
# 参数histtype='stepfilled'时可以使用参数alpha设置透明度
plt.hist(data, 5, color='blue', label='bins=5')
plt.hist(data, 7, color='purple', label='bins=7')
plt.xlabel('区间划分情况', fontproperties='simhei')
plt.ylabel('各区间内数据数量', fontproperties='simhei')
plt.title('直方图', fontproperties='simsun', fontsize=16)
plt.legend()
plt.show()
