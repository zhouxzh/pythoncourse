import matplotlib.pyplot as plt

# 月份和每月营业额
month = range(1, 13)
money = [5.2, 2.7, 5.8, 5.7, 7.3, 9.2, 18.7, 15.6, 20.5, 18.0, 7.8, 6.9]

plt.plot(month, money, 'r-.v', mfc='b', mec='y')
plt.xlabel('月份', fontproperties='simhei', fontsize=14)
plt.ylabel('营业额（万元）', fontproperties='simhei', fontsize=14)
plt.title('烧烤店2022年营业额变化趋势图', fontproperties='simhei', fontsize=18)
# 紧缩四周空白，扩大绘图区域可用面积
plt.tight_layout()

plt.show()
