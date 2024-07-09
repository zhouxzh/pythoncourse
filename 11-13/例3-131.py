import tkinter
from numpy import arange, sin, pi
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

root = tkinter.Tk()
root.title('matplotlib in TK')

# 设置图形尺寸与质量
fig = Figure(figsize=(5,4), dpi=100)
ax = fig.add_subplot(111)
t = arange(0.0, 3, 0.01)
s = sin(2*pi*t)
ax.plot(t, s)

# 把绘制的图形显示到tkinter窗口上
canvas = FigureCanvasTkAgg(fig, master=root)
##canvas.get_tk_widget().pack(side=tkinter.TOP,
##                            fill=tkinter.BOTH,
##                            expand=tkinter.YES)
# 把Matplotlib图形的导航工具栏显示到tkinter窗口上
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=tkinter.TOP,
                      fill=tkinter.BOTH,
                      expand=tkinter.YES)

# 定义并绑定键盘事件处理函数
def on_key_event(event):
    print(f'you pressed {event.key}')
    # 调用Matplotlib工具栏默认快捷键，演示用，可删除
    key_press_handler(event, canvas, toolbar)
canvas.mpl_connect('key_press_event', on_key_event)

# 按钮单击事件处理函数
def quit():
    # 结束事件主循环，并销毁应用程序窗口
    root.quit()
    root.destroy()
button = tkinter.Button(master=root, text='Quit', command=quit)
button.pack(side=tkinter.BOTTOM)

root.mainloop()
