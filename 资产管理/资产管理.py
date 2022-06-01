from sqlite3 import Row
import tkinter as tk
from tkinter.tix import COLUMN, ROW
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

win = tk.Tk()
win.title("资产管理")
win.geometry('800x500+300+200')  # 窗口创建位置是（300，200）
######################################################################
# 详细信息

area2 = tk.LabelFrame(win,
                      text='位置',
                      labelanchor="n",
                      bg=cl.Gray,
                      bd=5,
                      height=150)
area2.place(x=0, y=0)

for i in unit_list:
    for j in i:
        ck=tk.Checkbutton(area2, text=j)
        ck.grid(column=unit_list.index(i),row=i.index(j),sticky='w')
        ck.select()



# 将 selectmode 设置为多选模式，并为Listbox控件添加滚动条
listbox1 =tk.Listbox(win,selectmode = tk.BROWSE,height =25)
#listbox1.pack()
listbox1.place(x=10,y=200,width=150,relheight=0.6)
# 设置滚动条，使用 yview使其在垂直方向上滚动 Listbox 组件的内容，通过绑定 Scollbar 组件的 command 参数实现
s =tk. Scrollbar(listbox1)
listbox1.configure( yscrollcommand = s.set)
# 设置垂直滚动条显示的位置，使得滚动条，靠右侧；通过 fill 沿着 Y 轴填充
s.pack(side = tk.RIGHT,fill = tk.Y)
s.config(command = listbox1.yview)
for i,item in enumerate(range(1,50)):
    listbox1.insert(i,item)



area3 = tk.LabelFrame(win,
                      text='详细信息',
                      labelanchor="n",
                      bg=cl.Gray,
                      bd=5,
                      height=150)
area3.place(x=200, y=0)

for i in unit_list:
    for j in i:
        ck=tk.Checkbutton(area3, text=j)
        ck.grid(column=unit_list.index(i),row=i.index(j),sticky='w')
        ck.select()





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
        g = class_group(j, _window=area3, _pos=[x, y])
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