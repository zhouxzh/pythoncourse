import numpy as np
import matplotlib.pyplot as plt

# 1650985040为 2022年4月26日22:57的时间戳
np.random.seed(1650985040)
data = np.random.randint(0, 100, (50,50))
row = np.random.randint(0, 50, 5000)
col = np.random.randint(0, 50, 5000)
# 把部分元素值改为0
data[row, col] = 0
# 非0元素使用五角星表示，0使用空白表示
plt.spy(data, marker='*', markersize=4)
plt.show()
