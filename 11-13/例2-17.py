import numpy as np
import pandas as pd

# 模拟转盘100000次
data = np.random.ranf(100000)
# 奖项等级划分
category = (0.0, 0.08, 0.3, 1.0)
labels = ('一等奖', '二等奖', '三等奖')
# 对模拟数据进行划分
result = pd.cut(data, category, labels=labels)
# 统计每个奖项的获奖次数
result = pd.value_counts(result)

# 查看结果
print(result)