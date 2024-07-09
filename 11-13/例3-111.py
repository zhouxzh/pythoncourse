from numpy import linspace, sin, pi
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

x = linspace(-2*pi, 2*pi, 600)
y = sin(x)

fig = plt.figure()
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)
# 隐藏原来的所有坐标轴
ax.axis[:].set_visible(False)
# 增加自定义坐标轴，(0,0)第一个0表示维度，第二个0表示位置
ax.axis['x'] = ax.new_floating_axis(0, 0)
ax.axis['y'] = ax.new_floating_axis(1, 0)
# 设置轴上的刻度位置
ax.axis['x'].set_axis_direction('top')
ax.axis['y'].set_axis_direction('left')
# 空心箭头
ax.axis['x'].set_axisline_style('->', size=3)
# 实心箭头
ax.axis['y'].set_axisline_style('-|>', size=3)
ax.set_yticks([-1,-0.5,0,0.5,1])

ax.plot(x, y)
plt.show()
