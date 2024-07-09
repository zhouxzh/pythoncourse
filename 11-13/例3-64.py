from math import degrees
import numpy as np
import matplotlib.pyplot as plt

# 创建图形，设置尺寸，单位为英寸
fig = plt.figure(figsize=(10,6))
# 创建极坐标子图
ax = plt.subplot(111, projection='polar')
# 顺时针绘制
ax.set_theta_direction(-1)
# 设置正上方为0度，绘制第一个柱的起始位置
ax.set_theta_zero_location('N')

# 演示数据
r = np.arange(100, 800, 20)
theta = np.linspace(0, np.pi*2, len(r), endpoint=False)
np.random.seed(20220704)
# 绘制柱状图
ax.bar(theta, r,        # 角度对应位置，半径对应高度
       width=0.18,      # 每个柱的宽度
       color=np.random.random((len(r),3)),  # 随机颜色
       align='edge',    # 从指定角度的径向开始绘制
       bottom=100)      # 柱的底面沿半径方向开始的位置

# 在圆心位置显示文本
ax.text(np.pi*3/2-0.2, 90, 'Origin', fontsize=12)
# 在每个柱的顶部显示文本表示大小
for angle, height in zip(theta, r):
    # 计算文本的旋转角度
    deg = degrees(angle)
    rotation = -deg+90 if deg<180 else -deg-90
    ax.text(angle+0.03, height+105, str(height),
            fontsize=height/80, rotation=rotation)
    
# 不显示坐标轴和网格线，下面两行代码可以实现同样效果
# ax.set_rgrids([])
# ax.set_thetagrids([])
plt.axis('off')
# 紧凑布局，缩小外边距
fig.tight_layout()

plt.show()
# 调用上面的show()之后会创建一个新的图形
# 再调用plt.savefig()时会得到空白图形
# 所以使用fig.savefig()保存图形
fig.savefig('polarBar.png', dpi=480)
