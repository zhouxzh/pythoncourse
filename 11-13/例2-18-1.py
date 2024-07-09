import pandas as pd

df = pd.read_excel('电影导演演员.xlsx')        # 从Excel文件中读取数据
print(df)

pairs = []
for i in range(len(df)):                      # 遍历每一行数据
    actors = df.at[i, '演员'].split('，')      # 获取当前行的演员清单
    for actor in actors:                      # 遍历每个演员
        pair = (actor, df.at[i, '电影名称'])
        pairs.append(pair)
pairs = sorted(pairs, key=lambda item:int(item[0][2:]))
                                              # 按演员编号进行排序
print(pairs)

index = [item[0] for item in pairs]
data = [item[1] for item in pairs]
df1 = pd.DataFrame({'演员':index, '电影名称':data})
result = df1.groupby('演员', as_index=False).count()
                                              # 分组，统计每个演员的参演电影数量
print(result)

result.columns = ['演员', '参演电影数量']       # 修改列名
print(result)

print(result.nlargest(3, '参演电影数量'))   # 参演电影数量最多的3个演员
