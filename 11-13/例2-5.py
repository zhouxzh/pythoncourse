import pandas as pd

df1 = pd.read_excel('学生成绩.xlsx', sheet_name='一班',
                    names=['序号', '一班'])
df2 = pd.read_excel('学生成绩.xlsx', sheet_name='二班')
df2.columns = ['序号', '二班']
df = pd.merge(df1, df2, on='序号')
print(df)
