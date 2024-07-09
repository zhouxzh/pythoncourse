import matplotlib.pyplot as plt

colors = 'bgrcmyk'
for i in range(len(colors)):
    plt.bar(i, 3*i+1, color=colors[i])

plt.show()
