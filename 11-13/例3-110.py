from numpy import linspace, sin, pi
import matplotlib.pyplot as plt

# 统一设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

x = linspace(-2*pi, 2*pi, 600)
y = sin(x)

fig = plt.figure()
ax = fig.gca()

# 不显示右侧和顶部的直线
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置左边直线（y轴）的属性
# 坐标轴颜色
ax.spines['left'].set_color('red')
# 坐标轴宽度
ax.spines['left'].set_linewidth(2)
# 刻度在轴线左侧
ax.yaxis.set_ticks_position('left')
# 显示刻度的位置和文本
ax.yaxis.set_ticks([-1, -0.5, 0, 0.5, 1])
ax.yaxis.set_ticklabels(['-1', '-0.5', '0', '零点五', '一'])
# 刻度显示为红色
ax.tick_params(axis='y', colors='red')
# 设置左侧轴线位置
# 参数必须是元组(type, amount)
# ('data',0)表示数据为0的位置
ax.spines['left'].set_position(('data',0))
# 使用annotate在y轴顶端创建箭头
ax.annotate('', (0,1), xytext=(0,1.2),
            arrowprops={'arrowstyle':'<-',
                        'color':'red',
                        'linewidth':2})

# 设置底部直线（x轴）的属性
ax.spines['bottom'].set_color('green')
ax.spines['bottom'].set_linewidth(2)
ax.spines['bottom'].set_position(('data',0))
ax.annotate('', (6,0), xytext=(7.5,0),
            arrowprops={'arrowstyle':'<-',
                        'color':'green',
                        'linewidth':2})
ax.tick_params(axis='x', colors='green')

ax.plot(x, y)
fig.show()
