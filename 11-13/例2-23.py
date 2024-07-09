from time import time
import pandas as pd

# 读取数据，指定每列的数据类型
# 避免自动转换类型，还可以提高读取速度
df = pd.read_excel('小区业主用水情况.xlsx',
                   dtype={'日期':str, '房号':str,
                          '用水量（立方）':float})
start = time()
# 日期只保留年份，同时把列标签“日期”改为“年份”
df.日期 = df.日期.str.slice(0, 4)
df.columns = ['年份'] + list(df.columns.values[1:])
# 用水量列的缺失值替换为该小区整体月用水平均值
df.iloc[:,2].fillna(round(df.iloc[:,2].mean()), inplace=True)
# 按年份和房号分组，每个月的用水量求和
df = df.groupby(by=['年份', '房号'], as_index=False).sum()
#print(df.loc[df.年份=='2017',:].groupby(df.房号.str.slice(0,2)).max())
# 查找每年每个楼上用水总量最大的房号
data = []
for year in sorted(df.年份.unique()):
    for building_number in sorted(df.房号.str.slice(0,2).unique()):
        # 筛选指定年份和楼号的数据
        df_temp = df[(df.年份==year)&(df.房号.str.startswith(building_number))]
        # 该年份、楼号中，用水总量最大的房号
        data.extend(df_temp.nlargest(1, '用水量（立方）').values)
df_new = pd.DataFrame(data, columns=df.columns)
# print(df_new)
# 增加一列“楼号”，即房号的前两位
df_new['楼号'] = df_new.房号.str.slice(0,2)
print(df_new.pivot(index='楼号', columns='年份', values='房号'))
print(time()-start)
