import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['simhei']

# 读取数据，丢弃缺失值
df = pd.read_csv('data.csv', encoding='cp936')
df = df.dropna()

# 生成并保存营业额折线图
plt.figure()
df.plot(x='日期')
plt.xticks(rotation=10)
plt.savefig('first.jpg')

# 按月分组统计，生成并保存柱状图
plt.figure()
df1 = df.groupby(by=lambda irow: df.loc[irow, '日期'][:7]).sum()
df1.plot(kind='bar')
plt.xticks(rotation=20)
# print(df1)
plt.savefig('second.jpg')

# 查找涨幅最大的月份，写入文件
with open('maxMonth.txt', 'w') as fp:
    fp.write(df1.diff()['销量'].nlargest(1).keys()[0])

# 按季度统计，生成并保存饼状图
plt.figure()
df1.index = pd.to_datetime(df1.index).to_period('Q')
print(df1)
df1.groupby(level=0).sum().plot(y='销量', kind='pie')
plt.savefig('third.jpg')
