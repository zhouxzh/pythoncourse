import matplotlib.pyplot as plt

values = [1, 2, 3, 4, 5]
plt.stairs(values,
           edges=range(5,11),
           orientation='vertical',
           fill=False)
plt.show()
