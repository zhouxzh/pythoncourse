import numpy as np
import matplotlib.pyplot as plt

# 平均房价、波动范围，纯演示数据，不具有实际参考价值
prices = (12, 15, 11, 10, 8)
tolerance_p = (3, 4, 3, 2.5, 3.5)
# 平均月收入、波动范围，纯演示数据，不具有实际参考价值
wages = (6, 10, 7, 8, 6)
tolerance_w = (2, 5, 4, 4, 4)
index = np.arange(len(prices))
width = 0.4
cities = ('北京', '上海', '广州', '深圳', '杭州')
# 绘制房价柱状图和收入柱状图
# yerr用来指定误差范围，与结果图中的竖线对应
bars_prices = plt.bar(index, prices, width,
                      color='#999900', yerr=tolerance_p)
bars_wages = plt.bar(index+width, wages, width,
                     color='#990099', yerr=tolerance_w)
plt.xlabel('城市名称', fontproperties='simhei', fontsize=16)
plt.ylabel('金额（万元）', fontproperties='simhei', fontsize=16)
plt.title('收入与房价', fontproperties='simhei', fontsize=24)
plt.xticks(index+width/2, cities,
           fontproperties='simhei', fontsize=12)
# 创建图例
plt.legend([bars_prices, bars_wages], ['房价','月收入'], prop='simhei')

def add_text(bars, tol):
    for index, bar in enumerate(bars):
        # get_x()方法返回柱的左边缘x坐标
        x = bar.get_x() + width/2
        h = bar.get_height()
        # 在每个柱的误差线上下两侧显示文本，ha、va表示水平、垂直对齐方式
        plt.text(x, h+tol[index], str(h+tol[index]), color='k',
                 ha='center')
        plt.text(x, h-tol[index]-1, str(h-tol[index]), color='w',
                 ha='center', va='bottom')

add_text(bars_prices, tolerance_p)
add_text(bars_wages, tolerance_w)

plt.show()
