import numpy as np
import pandas as pd

# 创建写入器对象
writer = pd.ExcelWriter('result.xlsx', engine='openpyxl')
# 第一个DataFrame对象写入的起始列序号
start_col = 1
for i in range(500):
    dft = pd.DataFrame(np.random.randint(1, 10, (500,30)))
    dft.to_excel(writer, sheet_name='test',
                 # 指定从哪一列开始写入数据，默认值为0
                 startcol=start_col,
                 # 丢弃DataFrame对象的行标签和列标签
                 header=False, index=False)
    # 修改下一次开始写入数据的列位置
    start_col = start_col + dft.shape[1]
# 保存数据，关闭文件
writer.save()
writer.close()
