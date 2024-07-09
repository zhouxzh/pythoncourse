import pandas as pd
import matplotlib.pyplot as plt

def get_times(num):
    num = str(num)
    times = 0
    while True:
        # 几个数字能够组成的最大数
        big = int(''.join(sorted(num, reverse=True)))
        # 几个数字能够组成的最小数
        little = int(str(big)[::-1])
        difference = big - little
        times = times + 1
        if difference == 6174:
            return times
        num = str(difference)

# 各位互不相同的所有4位自然数
nums = filter(lambda num: len(set(str(num)))==4, range(1000, 10000))
df = pd.DataFrame({'num': list(nums)})
df['times'] = df.num.map(get_times)
df = df.groupby(by='times', as_index=False).count()

df.plot(x='times', kind='bar')
plt.yticks(list(df.num.values))
plt.show()
