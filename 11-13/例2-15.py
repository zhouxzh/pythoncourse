import pandas as pd
import matplotlib.pyplot as plt

# 读取数据文件中指定的列
df = pd.read_csv('testData.csv', usecols=[0,1,3,5,7])
# 分离类型A和B的数据，丢弃type列
dfA = df[df.type=='A'].drop('type', axis=1)
dfB = df[df.type=='B'].drop('type', axis=1)
# 修改列名，方便比较
dfA.columns = dfA.columns.map(lambda x: 'A_'+x)
dfB.columns = dfB.columns.map(lambda x: 'B_'+x)
dfA.index = range(len(dfA))
dfB.index = range(len(dfB))
# 绘制图形，指定同一个ax
fig = plt.figure()
ax = plt.gca()
dfA.plot(ax=ax)
dfB.plot(ax=ax)
# 显示图形
plt.show()
