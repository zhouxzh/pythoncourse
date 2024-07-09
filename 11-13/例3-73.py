import numpy as np
import matplotlib.pyplot as plt

labels = np.array(list('abcdefghij')) # 设置标签
data = np.array([11,4]*5)             # 创建模拟数据
dataLength = len(labels)              # 数据长度

# angles数组把圆周等分为dataLength份
angles = np.linspace(0,               # 数组第一个数据
                     2*np.pi,         # 数组最后一个数据
                     dataLength,      # 数组中数据数量
                     endpoint=False)  # 不包含终点
data = np.append(data, data[0])
angles = np.append(angles, angles[0]) # 首尾相接，使得曲线闭合
# 绘制雷达图
plt.polar(angles,                     # 设置角度
          data,                       # 设置各角度上的数据
          'rv--',                     # 设置颜色、线型和端点符号
          linewidth=2)                # 设置线宽

# 设置角度网格标签
plt.thetagrids(angles[:10]*180/np.pi, # 角度
               labels)                # 标签
# 设置角度起始方向和偏移量，正东方然后逆时针旋转17.5度开始绘制
plt.gca().set_theta_zero_location('E', offset=17.5)
# 设置填充色
plt.fill(angles,                      # 设置角度
         data,                        # 设置各角度上的数据
         facecolor='r',               # 设置填充色
         alpha=0.6)                   # 设置透明度
# 标记数值
for theta, r in zip(angles[:10], data[:10]):
    plt.text(theta, r, str(r), ha='center',
             va='center', color='b')
plt.ylim(0, 12)                       # 设置坐标跨度
# 不显示内部网格线
plt.grid(False)
# 不显示最外层网格线
# plt.gca().spines['polar'].set_visible(False)
# 不显示径向的数字
plt.yticks([])
# 不显示所有网格线和径向数字
plt.axis('off')

plt.show()                            # 显示绘图结果
