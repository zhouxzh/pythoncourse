import numpy as np
import pandas as pd

# 创建写入器对象
writer = pd.ExcelWriter('result.xlsx', engine='openpyxl')
# 第一个DataFrame对象写入的起始行位置，从第2行开始写，第1行保留为空行
start_row = 1
for i in range(500):
    dft = pd.DataFrame(np.random.randint(1, 10, (500,3)))
    dft.to_excel(writer, sheet_name='test',
                 # 指定从哪行开始写入数据，默认值为0，总行数不能超过1048576
                 startrow=start_row,
                 # 丢弃DataFrame对象的行标签和列标签
                 header=False, index=False)
    # 修改下一次开始写入数据的行位置
    start_row = start_row + dft.shape[0]
# 保存数据，关闭文件
writer.save()
writer.close()
