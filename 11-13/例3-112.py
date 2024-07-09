from numpy import linspace, sin, pi
import matplotlib.pyplot as plt

# 模拟数据，正弦曲线上的顶点
x = linspace(-2*pi, 2*pi, 600)
y = sin(x)

fig = plt.figure()
ax = fig.gca()

# 隐藏所有坐标轴直线
for key in ['left', 'right', 'top', 'bottom']:
    ax.spines[key].set_color('none')
    
# 设置左边直线（y轴）的属性
# 坐标轴宽度
ax.spines['left'].set_linewidth(2)
# 刻度在轴线左侧
ax.yaxis.set_ticks_position('left')
# 刻度的位置
ax.yaxis.set_ticks([-1, -0.5, 0, 0.5, 1])
# 刻度显示为红色
ax.tick_params(axis='y', colors='red')
# 设置左侧轴线位置
# 参数必须是元组(type, amount)
# ('data',0)表示数据为0的位置
ax.spines['left'].set_position(('data',0))
# 在坐标轴位置绘制一条带箭头的直线
# 前4个参数分别为x, y, dx, dy
ax.arrow(0, -1.2, 0, 2.4, color='red',
         linewidth=2, length_includes_head=True,
         head_width=0.2, head_length=0.3)

# 设置底部直线（x轴）的属性
ax.spines['bottom'].set_linewidth(2)
ax.spines['bottom'].set_position(('data',0))
ax.tick_params(axis='x', colors='green')
ax.arrow(-7, 0, 14, 0, color='green',
         linewidth=2, length_includes_head=True,
         head_width=0.05, head_length=0.3)

ax.plot(x, y)
fig.show()
