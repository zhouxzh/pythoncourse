import pandas as pd
from random import sample, choices

n = 20
firstNames = choices('赵钱孙李周吴郑王董孙', k=n)
lastNames = choices('一二三四五六七八九', k=n)
names = list({f+l for f, l in zip(firstNames, lastNames)})
df = pd.DataFrame({'姓名': names,
                   '分数': choices(range(70,90), k=len(names))})
print('原始数据'.center(30,'='), df, sep='\n')
# 分数最高的前5个人，分数相同的保留第一项
print('分数最高的前5个人，最后一个分数相同的话保留第一项'.center(30,'='))
print(df.nlargest(5, '分数'))
# 分数最高的前5个人，分数相同的保留最后一项
print('分数最高的前5个人，最后一个分数相同的话保留最后一项'.center(30,'='))
print(df.nlargest(5, '分数', keep='last'))
# 分数最高的前5个人，分数相同的保留所有人
print('分数最高的前5个人，最后一个分数相同的话保留所有人'.center(30,'='))
print(df.nlargest(5, '分数', keep='all'))
# 最高的前5个分数对应的信息
first5 = sorted(set(df.分数.values), reverse=True)[:5]
print('最高的前5个分数对应的信息'.center(30,'='))
print(df[df.分数.isin(first5)])
