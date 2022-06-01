import tkinter as tk
import color as cl
#####
unit_list = [['活动室', '室部', '校对组', '一组', '编辑组', '一体化'],
             ['学习室', '    ', '打印室', '三组', '二组', '仓库']]
cell_list = [
    [['无'], ['无2']],  #'活动室'
    [['a1'], ['a2']],  #'室部'
    [['1', '2', '3'], ['', '4', '5']],  #'校对组'
    [['1', '2', '3', '4', '5'], ['6', '7', '8', '9', '阿斯顿啊']],  #'一组'
    [['2', '0', '3', '4', '5'], ['6', '7', '8', '9', '阿斯顿啊']],  # 编辑组
    [['12', '2', '3', '4', '5'], ['6', '7', '8', '9', '阿斯顿啊']],  # 一体化
    [['无5'], ['学习室']],  #'学习室'
    [['无7'], ['无8']],  # 无
    [['gitlab', '123', '103'], ['T1300', 'T1200', 'T1100']],  # 打印室
    [['15', '2', '3', '4', '5'], ['6', '7', '8', '9', '阿斯顿啊']],  #'三组'
    [['81', '2', '3', '4', '5'], ['6', '7', '8', '9', '阿斯顿啊']],  #'二组对组'
    [['19', '2', '3', '4', '5'], ['6', '7', '8', '9', '阿斯顿啊', 'uy']]  #'仓库'
]

##############



# 最底层窗口
win= tk.Tk()
win.title("资产管理")
win.geometry('800x500+300+200')  # 窗口创建位置是（300，200）

# 列表
canvas = tk.Canvas(win, scrollregion=(0, 0, 1500, 600), bg=cl.Green)  #创建canvas
canvas.place(x=0, y=0, height=400, relwidth=1)

frame = tk.Frame(canvas, bg=cl.Blue)  #把frame放在canvas里
frame.place(x=0, y=0, relwidth=1)

vbar=tk.Scrollbar(canvas,orient=tk.VERTICAL,command=canvas.yview) #竖直滚动条
vbar.pack(anchor='e',side=tk.RIGHT,expand=1,fill = tk.Y) #frame的长宽，和canvas差不多的

hbar = tk.Scrollbar(canvas, orient=tk.HORIZONTAL, command=canvas.xview)  #水平滚动条
hbar.pack(anchor='s', side=tk.BOTTOM, fill=tk.X,
          expand=True)  #) #frame的长宽，和canvas差不多的

#print(canvas.winfo_x(),canvas.info(),canvas.size())
canvas.config(xscrollcommand=hbar.set)  # ,yscrollcommand=vbar.set) #设置
canvas.create_window((10, 10), window=frame, anchor='nw',
                     height=400)  #create_window
############################################################################################
# 详细信息
area2 = tk.LabelFrame(win,
                      text='详细信息',
                      labelanchor="w",
                      bg=cl.Gray,
                      bd=5,
                      height=50)
area2.place(x=0, y=400)
t_id=tk.Label(area2,text='sadasdas')
t_id.grid(row=0, column=0, padx=2, pady=10)
t_id=tk.Entry(area2)
t_id.grid(row=0, column=1, padx=2, pady=10)
button = tk.Button(area2, text='self.user', width=6)
button.grid(row=0, column=3, padx=2, pady=10)


class class_button():

    def __init__(self, _frame, _user, _pos=[0, 1]):
        # 常量
        self.frame = _frame
        self.user = _user
        if self.user != '':
            self.button = tk.Button(self.frame, text=self.user, width=6)
            self.button.grid(row=_pos[0], column=_pos[1], padx=2, pady=10)

        pass


class class_group():

    def __init__(self, _title, _window, _pos: list):
        self.bg = '#5CACEE'
        self.frame = tk.LabelFrame(_window,
                                   text=_title,
                                   labelanchor="n",
                                   bg=self.bg,
                                   bd=5,
                                   height=50)
        self.frame.grid(row=_pos[1], column=_pos[0], padx=2, pady=15)

        # button1=class_button(self.frame,'asd',[1,1])


f = tk.Frame(win, width=600, height=600, bg='#5CAC00')
units = []
for i in unit_list:
    for j in i:
        x = i.index(j)
        y = unit_list.index(i)
        g = class_group(j, _window=frame, _pos=[x, y])
        units.append(g)
        print(g.frame.grid_info())
units[-1].frame.grid(row=2, column=0, columnspan=3)
cells = []
for i in cell_list:  # 组 in 组列表
    for j in i:  # 排 in 组
        for k in j:  # 人 in 排
            unit = units[cell_list.index(i)]
            x = i.index(j)
            y = j.index(k)
            c = class_button(unit.frame, k, [x, y])
            cells.append(c)

win.mainloop()