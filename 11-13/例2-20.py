import pandas as pd

# 要读取的网页URL或本地HTML文件路径
url = r'https://mp.weixin.qq.com/s/RtFzEm2TnGHnLTHMz9T4Aw'
# 返回包含若干DataFrame的列表
# 网页上每个表格对应一个DataFrame，每个DataFrame自动以非负整数作为行标签和列标签
dfs = pd.read_html(url)

# 写入Excel文件，每个DataFrame对应一个工作表
with pd.ExcelWriter('result.xlsx') as wt:
    for index, df in enumerate(dfs, start=1):
        df.to_excel(wt, sheet_name=f'sheet{index}',
                    index=False, header=False)
