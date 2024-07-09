from math import log2
import numpy as np
from random import choices
import pandas as pd

# 设置输出结果列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

df = pd.DataFrame({'婚否': choices(('是','否'), k=20),
                   '工作否': choices(('是','否'), k=20),
                   '有车否': choices(('是','否'), k=20),
                   '收入水平': choices(('中','高','低'), k=20),
                   '是否有贷款': choices(('是','否'), k=20),
                   '结果': choices(('是','否'), k=20)})
print('====原始数据：', df, sep='\n')

# 原始数据总数量
total_length = len(df)

def get_entropy(values):
    '''计算一组数据的熵'''
    length = len(values)
    data = pd.value_counts(values).values / length
    return -(data * np.log2(data)).sum()

# 计算原始数据的熵
origin_entropy = get_entropy(df.结果.values)
print('====原始数据的熵：', origin_entropy, sep='\n')

# 存放使用每个列/特征进行分类后的信息熵
new_entropy = []

# 最后一列是分类结果，不用做分类特征
for column in df.columns[:-1]:
    # 该列所有唯一值
    unique_features = df[column].unique()
    # 存放使用该特征分类时每个子类的熵之和
    every_entropy = 0
    # 遍历每个唯一值，
    for feature in unique_features:
        # 获取数据，计算该类的熵
        values = df[df[column]==feature].结果.values
        every_entropy += len(values)/total_length*get_entropy(values)
    new_entropy.append((column, every_entropy))

gain = [(column,origin_entropy-e) for column, e in new_entropy]
print('====每个特征的信息增益：', *gain, sep='\n')
best_feature = max(gain, key=lambda item: item[1])[0]
print('====最佳分类特征：', best_feature, sep='\n')
print('====使用最佳特征进行分类：')
for value in df[best_feature].unique():
    print(df[df[best_feature]==value])
