from time import time
import pandas as pd

df = pd.read_excel('小区业主用水情况.xlsx',
                   dtype={'日期':str, '房号':str,
                          '用水量（立方）':float})
start = time()
# 日期列只保留年份
df.日期 = df.日期.str.slice(0, 4)
# 填充缺失值为所有住户用水平均值
df.iloc[:,2].fillna(round(df.iloc[:,2].mean()), inplace=True)
# 按年度和房号分组求和
df = df.groupby(by=['日期', '房号'], as_index=False).sum()
# 连接用水量和房号为一个字符串，用水量一定要在前
df['temp'] = df['用水量（立方）'].map(str).str.cat(df.房号, sep=',')
# 按年份和楼号分组，各组内按用水量和房号连接成的字符串求最大值
df = df.groupby(['日期', df.房号.str.slice(0,2)]).max()
df = df.drop(['房号','用水量（立方）'], axis=1).reset_index()
# 分离用水量和房号的字符串为两列
df = pd.concat([df.iloc[:,:2], df.temp.str.split(',', expand=True)],
               axis=1)
df.columns = ['日期', '楼号', '用水量（立方）', '房号']
df['用水量（立方）'] = df['用水量（立方）'].map(float)
# 透视表
print('各年度各楼单户最大用水量\n',
      df.pivot('楼号', '日期', '用水量（立方）'))
print('各年度各楼用水最多的房号\n',
      df.pivot('楼号', '日期', '房号'))
print(time()-start)
