import matplotlib.pyplot as plt

plt.pie([5, 10, 5, 10],
        explode=[0, 0, 0, 0.1],
        labels=list('ABCD'),
        autopct='{:.2f}%'.format,
        textprops={'fontsize':18, 'color':'k'},
        wedgeprops={'linewidth': 1, 'edgecolor': "black"})
# 纵横比相等，饼为正圆
plt.axis('equal')
 
plt.show()
