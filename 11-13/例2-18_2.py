import pandas as pd

df = pd.read_excel('电影导演演员.xlsx')
# 方法一
print(pd.value_counts('，'.join(df.演员.values).split('，')).nlargest(3))
# 方法二
df.演员 = df.演员.str.split('，')
print(df.explode('演员').groupby('演员').count()
      .nlargest(3, '电影名称')['电影名称'])
