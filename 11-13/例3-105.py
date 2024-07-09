from random import choices
import matplotlib.pyplot as plt

# 创建轴域，设置左边距、下边距、宽度、高度
ax = plt.axes([0.1, 0.2, 0.8, 0.7])
# 每个柱的位置、高度、刻度标签、颜色
x = range(5, 30, 5)
y = choices(range(1000,2000), k=5)
x_ticks = list('abcde')
colors = ('yellowgreen','pink','red','blue','green')
# 绘制每个柱
for xx, yy, cc, tick in zip(x,y,colors,x_ticks):
    ax.bar(xx, yy, width=3, color=cc, label=tick)

plt.xlabel('X')
plt.ylabel('Y')
plt.xticks(x, x_ticks)
plt.title('Title')

# 设置并显示图例，位于轴域下方
plt.legend(loc='upper left',
           bbox_to_anchor=(0.2,-0.1),
           ncol=len(x))
# 显示图形
plt.show()
