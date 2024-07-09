import matplotlib.pyplot as plt

# 函数语法为：broken_barh(xranges, yrange, *, data=None, **kwargs)
# 第一个参数为x轴上的多个分段区间，每个区间格式为(start, width)
# 第二个参数为y轴上的起始位置和跨度，格式为(start, height)
plt.broken_barh([(1,2), (11,1)], (5,2),
                facecolors='blue')
plt.broken_barh([(3,2), (8,3)], (20,2),
                facecolors=('r', 'g'), alpha=0.7)
plt.broken_barh([(5,3)], (30,2),
                facecolors='#668844')
plt.ylim((0,40))
plt.xlabel('月份', fontproperties='simhei')
plt.ylabel('温度（摄氏度）', fontproperties='simhei')
plt.title('某城市平均温度', fontproperties='simhei')
plt.xticks(range(1,13))
plt.yticks(range(0, 45, 5))
plt.show()
