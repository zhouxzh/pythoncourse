import numpy as np
import matplotlib.pyplot as plt

# 进价与零售价
base_price, sale_price = 49, 75

# 顾客可能的购买数量，限购30件
numbers = np.arange(1, 31)
# 与每个购买数量对应的实际单价
real_price = sale_price * (1 - 0.01*numbers)
# 与每个购买数量对应的商场盈利情况
earns = np.round(numbers * (real_price-base_price), 2)
# 与每个购买数量对应的顾客总消费
total_consumption = np.round(numbers * real_price, 2)
# 与每个购买数量对应的顾客节省情况
saves = np.round(numbers * (sale_price-real_price), 2)

# 绘制商家盈利和顾客节省的折线图
plt.plot(numbers, earns, label='商家盈利', lw=3,
         color='red')
plt.plot(numbers, total_consumption, ls='--',
         label='顾客总消费', color='#66ff33')
plt.plot(numbers, saves, label='顾客节省', ls='-.',
         color='#000088')
# 设置坐标轴标签文本
plt.xlabel('顾客购买数量（件）', fontproperties='simhei')
plt.ylabel('金额（元）', fontproperties='simhei')
# 设置图形标题
plt.title('数量-金额关系图', fontproperties='STKAITI',
          fontsize=20)
# 创建字体，设置图例
plt.legend(prop='STKAITI')

# 计算并标记商家盈利最多的批发数量
maxEarn = earns.max()
bestNumber = numbers[earns==maxEarn][0]
# 散点图，在相应位置绘制一个红色五角星
plt.scatter(bestNumber, maxEarn, marker='*', color='red', s=240)
# 使用annotate()函数在指定位置进行文本标注
plt.annotate(xy=(bestNumber,maxEarn),                # 箭头终点坐标
             xytext=(bestNumber-1,maxEarn+200),      # 箭头起点坐标
             text=str((bestNumber,maxEarn)),         # 显示的标注文本
             arrowprops=dict(width=3,headlength=5))  # 箭头样式
# 本例绘制的示意图不适合设置纵横比相等
# plt.gca().set_aspect('equal')
# 显示图形或保存图形
plt.show()
# plt.savefig('商场优惠活动.jpg', dpi=480)
