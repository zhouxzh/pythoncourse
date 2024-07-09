import matplotlib.pyplot as plt

# 每个月的销售额
month = [5.2, 2.7, 5.8, 5.7, 7.3, 9.2, 18.7,
         15.6, 20.5, 18.0, 7.8, 6.9]
# 按季度分组求和
quarter = list(map(lambda i:sum(month[i:i+3]),
                   range(0,len(month),3)))
# 外圈饼状图
plt.pie(month, radius=1, autopct='{:.1f}%'.format,
        pctdistance=0.85,
        labels=[f'{i}月' for i in range(1,13)],
        labeldistance=1.01, textprops={'family':'simhei'})
# 内层饼状图
patches, texts, autotexts = plt.pie(quarter, radius=0.7,
                                    autopct='{:.1f}%'.format,
                                    pctdistance=0.7)
# print(autotexts)
# 最内层的空心圆
plt.pie([1], radius=0.4, colors=[plt.gca().get_facecolor()])
# 图形标题
plt.title('月份/季度销售额', fontproperties='simhei', fontsize=18)
# 为中间层的环创建图例
plt.legend(patches, ['一季度', '二季度', '三季度', '四季度'], prop='simsun',
           title='内圈图例', title_fontproperties='microsoft yahei')
plt.show()
