import tkinter as tk
from turtle import width
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


class C_window():

    def __init__(self) -> None:
        # 最底层窗口
        self.base_win = tk.Tk()
        self.base_win.title("资产管理")
        screenwidth = self.base_win.winfo_screenwidth()
        screenheight = self.base_win.winfo_screenheight()
        self.base_win.geometry('800x600+%d+%d' % ((screenwidth - 750) / 2,
                                                  (screenheight - 600) / 2))

        ########################################################################
        # 分组
        self.area1 = tk.LabelFrame(self.base_win, text='组 别', labelanchor="n")
        self.area1.grid(row=0, column=0)
        self.area1_add_ctrl()
        ########################################################################
        # 状态
        self.area2 = tk.LabelFrame(self.base_win, text='状态 ', labelanchor="w")
        self.area2.grid(row=0, column=1, padx=50, sticky=tk.N)
        self.area2_add_ctrl()
        ########################################################################
        # 列表
        self.listbox1 = tk.Listbox(self.base_win)
        self.listbox1.place(y=190, x=5, width=130, relheight=0.65)
        self.listbox1_add_ctrl()
        ########################################################################
        # 详细信息
        self.area3 = tk.LabelFrame(self.base_win, text='详细信息')
        self.area3.place(x=150, y=45, relwidth=0.79, relheight=0.9)
        self.area3_add_ctrl()
        ########################################################################

    def area1_add_ctrl(self):
        self.area1.config(bg=cl.Gray, bd=5, font=('微软雅黑', 10, 'bold'))
        win = self.area1
        ###################################
        room = ['学习室', '室部', '打印室', '校对', '三组', '一组', '二组', '编辑', '仓库', '一体化']
        self.cks1 = []
        for i in room:
            ck = tk.Checkbutton(win, text=i, name=i)
            id = room.index(i)
            ck.grid(column=id - int(id / 2) * 2, row=int(id / 2), sticky='w')
            ck.select()
            self.cks1.append(ck)

            print('len ck1', len(self.cks1), hash(ck))

        ####################################
        ck_all = tk.Checkbutton(win, text='全选')
        ck_all.grid(column=1, row=int(len(room) / 2), sticky='w')
        ck_all.select()

    def area2_add_ctrl(self):
        self.area2.config(bd=5, font=('微软雅黑', 10, 'bold'))
        win = self.area2
        ###################################
        status = ['在用', '闲置', '待报废', '已上交']
        self.cks2 = []
        for i in status:
            self.cks2.append(tk.Checkbutton(win, text=i, name=i))
            id = status.index(i)
            self.cks2[-1].grid(column=id, row=0, sticky='w')
            self.cks2[-1].select()
            print('len ck2', len(self.cks2), hash(self.cks2[-1]))

        self.cks2[-1].deselect()
        ##############################################
        tk.Label(win, text=' ').grid(row=0, column=4, padx=10)
        ##############################################
        bt_add = tk.Button(win, text='新增', bg=cl.Cyan)
        bt_add.grid(row=0, column=5, ipadx=10, padx=10)
        bt_edit = tk.Button(win, text='修改', bg=cl.Cyan)
        bt_edit.grid(row=0, column=6, ipadx=10, padx=10)
        bt_del = tk.Button(win, text='删除', bg=cl.Cyan)
        bt_del.grid(row=0, column=7, ipadx=10, padx=10)
        bt_save = tk.Button(win, text='保存', bg=cl.Cyan)
        bt_save.grid(row=0, column=8, ipadx=10, padx=10)

    def listbox1_add_ctrl(self):
        self.listbox1.config(borderwidth=5, height=175, width=33)
        win = self.listbox1
        s = tk.Scrollbar(win)
        win.configure(yscrollcommand=s.set)
        s.pack(side=tk.RIGHT, fill=tk.Y)
        s.config(command=win.yview)
        for i, item in enumerate(range(1, 30)):
            win.insert(i, item)

    def area3_add_ctrl(self):
        self.area3.config(labelanchor="nw", bg=cl.Magenta, bd=5)
        win = self.area3
        labels = ['ID', '启用时间', '品牌', '位置', '型号', '用户名称', '网络类型']
        labels = labels + ['MAC', '网线接口', 'IP', '保密系统']
        tk.Label(win, text='', name='bt_').grid(row=0, column=2, padx=15)
        #################################################################
        for i in labels:
            id = labels.index(i)
            x = int(id / 2)
            y = (id - x * 2) * 3
            l = tk.Label(win, text=i, name='lab_' + i, font=('微软雅黑', 15))
            l.grid(row=x, column=y, pady=5)
        ##################################################################
        txt_id = tk.Entry(win, width=15, font=('微软雅黑', 15))
        txt_id.grid(padx=5, row=0, column=1)
        txt_pp = tk.Entry(win, width=15, font=('微软雅黑', 15))
        txt_pp.grid(padx=5, row=1, column=1)
        txt_xh = tk.Entry(win, width=15, font=('微软雅黑', 15))
        txt_xh.grid(padx=5, row=2, column=1)

        txt_date = tk.Entry(win, width=15, font=('微软雅黑', 15))
        txt_date.grid(padx=5, row=0, column=4)
        ######

        #######
        txt_pos = tk.Entry(win, width=15, font=('微软雅黑', 15))
        txt_pos.grid(padx=5, row=2, column=1)

        txt_user = tk.Entry(win, width=15, font=('微软雅黑', 15))
        txt_user.grid(padx=5, row=2, column=4)
        ###############
        tk.Label(win, text='', name='k2', font=('微软雅黑', 15)).grid(row=10, column=0, padx=15)
        tk.Label(win, text='备注', name='k3', font=('微软雅黑', 15)).grid(row=11, column=0, padx=15)
        txt_bz = tk.Entry(win, width=15, font=('微软雅黑', 15))
        txt_bz.grid( row=12, column=0,columnspan=5,ipadx=200)
        self.listbox2 = tk.Listbox(win)
        self.listbox2.grid( row=13, column=0,columnspan=5,ipadx=200)

        ##################################################### AA-BB-CC-99-88-77

    def line(self, str1, str2):
        win = 0
        lab_id = tk.Label(win, text='ID', name='bt_id')
        lab_id.grid(row=0, column=1)


'''
win = tk.Tk()
ck = tk.Checkbutton(win, text='i')
ck.deselect()
'''


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


mywin = C_window()
mywin.base_win.mainloop()
