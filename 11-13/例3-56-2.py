from collections import Counter
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
result = Counter(map(get_times, nums))

plt.bar(result.keys(), result.values())
plt.yticks(list(result.values()))
plt.show()
