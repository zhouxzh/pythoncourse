import pandas as pd

# 依次读取多个相同结构的Excel文件并创建DataFrame
dfs = []
for fn in ('1.xlsx', '2.xlsx', '3.xlsx', '4.xlsx'):
    dfs.append(pd.read_excel(fn))
# 将多个DataFrame合并为一个
df = pd.concat(dfs)
# 写入Excel文件，不包含索引数据
df.to_excel('result.xlsx', index=False)
