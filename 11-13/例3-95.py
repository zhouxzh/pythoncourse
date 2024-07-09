import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

# 创建DataFrame结构
df = pd.DataFrame({'男士': (450,800,200),
                   '女士': (150,100,300)})
# 创建三维图形
ax = plt.subplot(projection='3d')
# 绘制三维柱状图
ax.bar3d([0]*3, range(3), [0]*3,
          0.1, 0.1, df['男士'].values,
          color='r')
ax.bar3d([1]*3, range(3), [0]*3,
          0.1, 0.1, df['女士'].values,
          color='b')

# 设置坐标轴刻度和文本
ax.set_xticks([0,1])
ax.set_xticklabels(['男士','女士'], fontproperties='simhei')
ax.set_yticks([0,1,2])
ax.set_yticklabels(['从不闯红灯','跟从别人闯红灯','带头闯红灯'],
                     fontproperties='simhei')
# 设置z轴标签
ax.set_zlabel('人数', fontproperties='simhei')

plt.show()
