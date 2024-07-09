import pandas as pd

df1 = pd.DataFrame({'A': [None, 3, 5], 'B': [3, None, None]},
                   index=['x1','x2','x3'])
df2 = pd.DataFrame({'A': [8, None, 8, 9], 'B': [None, 6, 6, 9],
                    'C': [666, None, 999, None]},
                   index=['x1','x2','x3', 'x4'])
print('===演示数据：', df1, df2, sep='\n')
# 使用参数other中的值更新当前对象中的缺失值
print('===combine_first()方法处理结果：', df1.combine_first(df2), sep='\n')
# 以另一个DataFrame对象为准，原地修改当前DataFrame中的缺失值
# 保留原始DataFrame对象的行标签和列标签
# overwrite=False时只更新当前DataFrame中的缺失值
df1.update(df2, overwrite=False)
print('===update()方法处理结果：', df1, sep='\n')
