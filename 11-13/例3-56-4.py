import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pgf import FigureCanvasPgf

plt.rcParams['text.usetex'] = True
plt.rcParams['pgf.rcfonts'] = False
plt.rcParams['pgf.preamble'] = r'\usepackage{color,xeCJK}'
mpl.backend_bases.register_backend('pdf', FigureCanvasPgf)

mpl.use('pgf')

def get_times(num):
    if num == 6174:
        return 0
    num = str(num)
    times = 0
    while True:
        big = int(''.join(sorted(num, reverse=True)))
        little = int(str(big)[::-1])
        diff = big - little
        times = times + 1
        if diff == 6174:
            return times
        num = str(diff)

# 各位数字互不相同的所有4位自然数
nums = filter(lambda num: len(set(str(num)))==4, range(1000,10000))
df = pd.DataFrame({'num': list(nums)})
# 增加一列，计算每个4位数需要多少次才能变为6174
df['times'] = df.num.map(get_times)
# 分组，统计每个次数对应的4位自然数数量
df = df.groupby(by='times', as_index=False).count()

fig, ax = plt.subplots()
df.plot(x='times', kind='bar', ax=ax)
# 设置x轴刻度加粗
plt.xticks(range(8), [rf'\textbf{i}' for i in range(8)])
# 设置y轴不均匀刻度、加粗、斜体
plt.yticks(list(df.num.values),
           [r'\textbf{\textit{'+str(i)+'}}' for i in df.num.values])
plt.xlabel('times', fontsize=16)
# y轴标签第一个单词字体加粗
plt.ylabel(r'\textbf{number}-of-numbers', fontsize=16)
# 标题第一个单词斜体，第三个单词斜体、标红，最后一组数字加粗、变大
# fontsize命令第一个参数为字号，第二个参数为行距
plt.title(r'\emph{次数} of \emph{\textcolor{red}{numbers}}'
          r' to become \fontsize{28pt}{24pt}\textbf{6174}',
          fontsize=20)

plt.savefig('result.pdf')
