import pandas as pd

fn = '学生测试成绩.xlsx'
df = pd.read_excel(fn)
result = df.groupby(['姓名','课程'], as_index=False).max()
result.to_excel('成绩统计结果.xlsx', sheet_name='各科最高分', index=False)
