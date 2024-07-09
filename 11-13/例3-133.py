from random import randomfrom math import sin, cos, pifrom tkinter.messagebox import showinfoimport matplotlib.pyplot as pltfrom matplotlib.widgets import Button# 设置图形上的中文字体，支持在图形上显示中文plt.rcParams['font.sans-serif'] = ['SimHei']# 划分转盘上的区域data = {'一等奖':0.08, '二等奖':0.22, '三等奖':0.7}fig = plt.figure()# 创建轴域，用来绘制饼状图和折线图ax1 = plt.axes([0.1, 0.15, 0.8, 0.8])# 绘制饼状图，模拟转盘ax1.pie(data.values(), labels=data.keys(), radius=1)ax1.plot([0,1], [0,0], lw=3, color='white')def start(event):    # 禁用按钮，避免重复响应鼠标单击    buttonStart.set_active(False)    # 用来控制指针位置的变量    position = 0    step = random() * 2    ax1.lines.clear()    ax1.plot([0,cos(position)], [0,sin(position)],             lw=3, color='white')    # 强制更新图形    plt.draw_all(True)    # 模拟转盘上指针的转动    for i in range(150):        # 不断减小step的值，模拟指针越转越慢        if i%15 == 0:            step = max(0, step-0.2)        # 如果已经转的很慢了，提前结束循环        if step < 1e-2:            break        position = position + step        # 暂停，参数越小，转的越快        plt.pause(0.05)        # 删除图形上的所有直线        ax1.lines.clear()        # 重新绘制一条直线，模拟指针的转动        # [0, cos(position)]表示直线起点和终点的横坐标        # [0, sin(position)]表示直线起点和终点的纵坐标        # lw=3表示设置指针的宽度为3个像素        # color='white'表示绘制白色直线来模拟指针        ax1.plot([0,cos(position)], [0,sin(position)],                lw=3, color='white')        # 强制更新图形        plt.draw_all(True)    # 启用按钮    buttonStart.set_active(True)    position = position % (2*pi)    ratio = position / (2*pi)    # 判断所中奖项等级，弹出消息框提示    if ratio > data['一等奖']+data['二等奖']:        showinfo('恭喜', '三等奖')    elif ratio > data['一等奖']:        showinfo('恭喜', '二等奖')    else:        showinfo('恭喜', '一等奖')  # 创建子图，放置按钮ax2 = plt.axes([0.45, 0.1, 0.1, 0.05])buttonStart = Button(ax2, 'Start', color='white',                     hovercolor='red')buttonStart.on_clicked(start)plt.show()