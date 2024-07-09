import logging
from collections import Counter
import jieba
import pandas as pd
import matplotlib.pyplot as plt

# 不显示jieba库加载和分词的提示信息
jieba.setLogLevel(logging.INFO)
plt.rcParams['font.sans-serif'] = 'stkaiti'

txt_file = 'news.txt'
# 读取文件内容
with open(txt_file, encoding='utf8') as fp:
    content = fp.read()
# 分词，过滤掉标点符号和单个字，然后提取出现次数最多的前10个词
words = filter(lambda word: len(word)>1, jieba.cut(content))
freq = pd.Series(Counter(words)).nlargest(10)
# 绘制柱状图
freq.plot(kind='bar')

plt.title('十大热词')
# 设置x轴刻度标签旋转30度
plt.xticks(rotation=30)
plt.ylabel('出现次数')
plt.show()
