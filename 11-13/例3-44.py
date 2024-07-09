import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(0, 8, 100)
x = 8 * np.sin(t) ** 3
y = 15 * np.cos(t) - 5*np.cos(2*t) - 4*np.cos(3*t) - np.cos(4*t)
# marker其他可能的类似Latex符号还有：
# '$\forall$','$\exists$','$\lnot$','$\hbar$','$\triangle$',
# '$\nabla$','$\partial$','$\varnothing$','$\emptyset$',
# '$\aleph$','$\angle$','$\measuredangle$','$\surd$',
# '$\eth$','$\mho$','$\complement$','$\ell$','$\dots$',
# '$\vdots$','$\ddots$','$\top$','$\bot$','$\diamondsuit$',
# '$\heartsuit$','$\clubsuit$','$\spadesuit$'
# 为防止反斜线与后面的字符被解释为转义字符，建议使用原始字符串
plt.scatter(x, y, s=60, c='r', alpha=0.6, marker=r'$\clubsuit$')
plt.axis('off')
plt.show()
