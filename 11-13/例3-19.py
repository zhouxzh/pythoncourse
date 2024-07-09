import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 300)
y1 = np.sin(x) ** 2
y2 = np.cos(x) ** 3
y3 = np.cos((x+np.pi/2)/2) + 0.3

# 绘制折线图，在label属性中使用公式，将会显示在图例中
plt.plot(x, y1, 'r-', lw=2, label='$sin^2(x)$')
plt.plot(x, y2, 'g--', lw=2, label='$cos^3(x)$')
plt.plot(x, y3, 'b-.', lw=1,
         label=r'$cos(\frac{x+\pi/2}{2})+0.3$')
# 在图形中输出文本和公式，把需要渲染为公式的字符串放在两个$之间
plt.text(0, 1.3, 'Demo Equation:$y=ax^3+bx^2+c$')
plt.text(0, 1.1, (r'Combination Number:$\binom{k}{n}='+
                  r'\binom{k}{n-1}+\binom{k-1}{n-1}$'))
# 在注解中显示公式
plt.annotate('$sin^2(x)$', xy=(12.2,np.sin(12.2)**2),
             xytext=(11,-0.25),
             # 实心箭头
             arrowprops={'arrowstyle':'-|>'})
plt.annotate('$cos^3(x)$', xy=(8,np.cos(8)**3),
             xytext=(6.5,-0.75),
             # 空心箭头
             arrowprops={'arrowstyle':'<-'})
# 在坐标轴标签和图形标题中显示公式
plt.ylabel(r'$\frac{\pi}{4}$', rotation=0)
plt.title(r'$(a-b)\times(c-d)$')
# 创建图例，显示在图形左下角
plt.legend(loc='lower left')
plt.show()
