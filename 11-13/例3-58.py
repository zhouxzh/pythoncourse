import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 创建图形，设置背景色
fig = plt.figure(facecolor='#eeeeee')
# 创建子图，设置背景色，下面两行的方式都可以
# ax = plt.axes(facecolor='#ffaaee')
ax = fig.add_axes((0.1,0.1,0.88,0.82), facecolor='#ffaaee')
df = pd.DataFrame({'男士': (450,800,200),
                   '女士': (150,100,300)})
# 绘制柱状图，以DataFrame对象的行标签为每个柱的x坐标
df.plot(kind='bar', ax=ax, color=['#ff6666','#6666ff'])

# 设置x轴刻度位置和文本
plt.xticks([0,1,2],
           ['从不闯红灯', '跟从别人闯红灯', '带头闯红灯'],
           color='black',
           rotation=20)                # 旋转刻度的文本
# 设置y轴只在有数据的位置显示刻度
plt.yticks(list(df['男士'].values) + list(df['女士'].values))
plt.ylabel('人数', fontsize=14)
plt.title('集体过马路方式',  fontsize=20)
# 创建和设置图例字体
plt.legend(fontsize=8)

# 行标题单元格颜色
rowColours = [[0.6,0.6,0.9], [0.8,0.6,0.8]]
# 列标题单元格颜色
colColours = [[0.69,0.8,0.7], [0.53,0.72,0.82], [0.93,0.73,0.63]]
# 表格主体单元格颜色
cellColours = [['#eeffee','#ffeeee','#eeeeff']] * 2
# 绘制表格
plt.table([df.男士.values, df.女士.values],
          rowLabels=['男士','女士'], rowColours=rowColours,
          colLabels=['从不闯红灯','跟从别人闯红灯','带头闯红灯'],
          colColours=colColours, cellColours=cellColours,
          fontsize=16,                 # 字号
          cellLoc='center',            # 居中
          bbox=[0.55,0.75,0.45,0.15])  # 表格在图形中的位置和大小

plt.show()
