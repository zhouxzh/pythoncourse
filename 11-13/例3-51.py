import matplotlib.pyplot as plt

left = range(6)
bottom = range(6)
width, height = 0.5, 2

# 使用动漫风格，参数表示变形程度
with plt.xkcd(2):
    plt.bar(left, height, width, bottom)
plt.title('bars with different bottom', fontsize=18)
plt.xlabel('position')
plt.ylabel('start-stop')
plt.show()
