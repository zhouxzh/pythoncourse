import numpy as np
import matplotlib.pyplot as plt

# 月份和每月营业额
month = list(range(1, 13))
money = [5.2, 2.7, 5.8, 5.7, 7.3, 9.2,
         18.7, 15.6, 20.5, 18.0, 7.8, 6.9]

# 绘制折线图，设置颜色和线型
plt.plot(month, money, 'r-.')
# 绘制散点图，设置颜色、符号和大小
plt.scatter(month, money,
            # 随机颜色，每个散点符号的颜色不同
            # 每行表示一个散点的颜色，每行3个数字分别表示红、绿、蓝分量
            c=np.random.random((len(month),3)),
            # 散点符号与大小
            marker='*', s=128)
plt.xlabel('月份', fontproperties='simhei', fontsize=14)
plt.ylabel('营业额（万元）', fontproperties='simhei', fontsize=14)
plt.title('烧烤店2022年营业额变化趋势图',
          fontproperties='simhei', fontsize=18)
# 紧缩四周空白，扩大绘图面积
plt.tight_layout()

plt.show()
