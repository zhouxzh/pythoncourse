import matplotlib.pyplot as plt

plt.step(range(10), [3,8,4,7,2,9,3,5,8,5], 'g-.*',
         # 定义台阶位置，可以为'pre'、'post'、'mid'，默认值为'pre'
         where='mid')
plt.show()
