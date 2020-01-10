#导入模块
import tkinter as tk
import tkinter.font as font
import tkinter.messagebox as mesbox
import pickle
from tkinter import  ttk
from PIL import ImageTk,Image
import time
import re
import math
import decimal


from1=tk.Tk()
from1.title("油品损耗计算及信息存储系统v6.0.1")
w=590
h=500
sw=from1.winfo_screenwidth()
sh=from1.winfo_screenheight()
x=sw/2-w/2;y=sh/2-h/2-50
from1.geometry("%dx%d+%d+%d"%(w,h,x,y))

#定义函数
def btn1click():
    username=entry1.get()
    password=entry2.get()
    try:
        with open("usrs_info.pickle","rb") as usr_file:
            usrs_info = pickle.load(usr_file)
    except EOFError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
            usr_file.close()
    if username in usrs_info:
        if password == usrs_info[username]:
            from1.destroy()
            class Application_ui(tk.Frame):
                # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
                def __init__(self, master=None,*args, **kwargs):
                    tk.Frame.__init__(self, master)
                    self.master.title('油品损耗计算及信息存储系统v6.0.1')

                    w =1050
                    h=650
                    sw = self.master.winfo_screenwidth()
                    sh = self.master.winfo_screenheight()
                    x= sw/2-w/2;y =sh/2-h/2-50
                    self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))
                    self.createWidgets()







                def createWidgets(self):
                    self.top = self.winfo_toplevel()
                    # lab5=ttk.Button(self.top,text="NNNN")
                    #                     # lab5.place(x=10,y=10)
                    #                     # self.style = ttk.Style()
                    #                     # self.style.configure('Red.TLabelframe.Label', font=('courier', 20, 'bold'))
                    #                     # self.style.configure('Red.TLabelframe.Label', foreground='red')
                    #                     # self.style.configure('Red.TLabelframe.Label', background='blue')
                    #                     # 边距尺寸
                    self.TabStrip1 = ttk.Notebook(self.top)
                    # 标签的长宽以及位置
                    self.TabStrip1.place(relx=0.0, rely=0, relwidth=0.99, relheight=0.92, x=5, y=5)

                    from1.s14 = tk.PhotoImage(file="首页1.png")
                    from1.s15 = tk.PhotoImage(file="静储1.png")
                    from1.s16 = tk.PhotoImage(file="船1.png")
                    from1.s17 = tk.PhotoImage(file="罐车经1.png")
                    from1.s18 = tk.PhotoImage(file="罐车未1.png")
                    from1.s19 = tk.PhotoImage(file="罐车1.png")
                    from1.s20 = tk.PhotoImage(file="拱顶罐1.png")
                    from1.s21 = tk.PhotoImage(file="无喷涂1.png")
                    from1.s22 = tk.PhotoImage(file="无喷1.png")
                    from1.s23 = tk.PhotoImage(file="喷涂损耗1.png")
                    from1.s24 = tk.PhotoImage(file="喷涂1.png")
                    from1.s31 = tk.PhotoImage(file="增加1.png")
                    from1.s32 = tk.PhotoImage(file="计算1.png")
                    from1.s33 = tk.PhotoImage(file="删除1.png")
                    from1.s34 = tk.PhotoImage(file="输出1.png")


                    self.TabStrip1__Tab0 = ttk.Frame(self.TabStrip1)
                    # self.TabStrip1__Tab1Lbl = ttk.Label(self.TabStrip1__Tab1, text='Please add aaa code.',foreground="blue",font="Aria 20")
                    #  self.TabStrip1__Tab1Lbl.place(relx=0.1, rely=0.5)
                    self.TabStrip1.add(self.TabStrip1__Tab0, text=' 首页 ',image=from1.s14,compound="left")
                    # 窗口图片











                    self.TabStrip1__Tab1 = ttk.Frame(self.TabStrip1)
                    # self.TabStrip1__Tab1Lbl = ttk.Label(self.TabStrip1__Tab1, text='Please add aaa code.',foreground="blue",font="Aria 20")
                    #  self.TabStrip1__Tab1Lbl.place(relx=0.1, rely=0.5)
                    self.TabStrip1.add(self.TabStrip1__Tab1,text='有喷涂损耗',image=from1.s24,compound="left")
                    def lbox1click(e):
                        w = e.widget
                        global t
                        # 定义全局变量，可以用到下面的定义事件中
                        t = w.curselection()
                        pass
                    def addclick():
                        lbox1.insert(tk.END, "  " + youlei.get() + "                                " +
                                     ent1.get() + "                                               "
                        +ent2.get() +

                                     "                                            " + ent3.get())
                        pass
                    def xiugaiclick():
                        pass
                    def sanchuclick():
                        lbox1.delete(t)
                        pass
                    def go(*args):
                        pass
                    def printclick():
                        mesbox.showinfo('输出成功','数据已输出成功，请在根目录下查看！')

                        i = 1
                        while i < 100:
                            result = str(lbox1.get(i))
                            with open('有喷涂损耗计算.text', 'a') as feil_handle:
                                feil_handle.write(result)
                                feil_handle.write("\n")
                            i += 1
                        pass


                    # 在如listbox控件
                    lbox1 = tk.Listbox(self.TabStrip1__Tab1,background="#89c291",height=28,width=105,font=('Arial', 10))
                    lbox1.place(x=20,y=50)
                    lbox1.bind("<<ListboxSelect>>", lbox1click)

                    #滚动条
                    scrollbar1 = ttk.Scrollbar(lbox1,command=lbox1.yview)
                    scrollbar1.place(x=718, y=0,height=480)
                    lbox1.config(yscrollcommand=scrollbar1.set)
                    scrollbar1.config(command=lbox1.yview)
                    # Adding a Combobox
                    youlei = tk.StringVar()
                    youlei = ttk.Combobox(self.TabStrip1__Tab1, width=11, textvariable=youlei)
                    youlei['values'] = ('石脑油', '汽  油', '柴  油', '煤  油',"蜡  油")
                    youlei.place(x=890,y=130)
                    youlei.current(0)  # 设置初始显示值，值为元组['values']的下标
                    youlei.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
                    # youlei.config(state='readonly')  # 设为只读模式
                    # 载入单行文本框
                    ent1variable=tk.StringVar()
                    ent1 = tk.Entry(self.TabStrip1__Tab1,width=14,textvariable=ent1variable)
                    ent1.place(x=890, y=180)
                    ent1variable.set("6.000")

                    ent2variable=tk.StringVar()
                    ent2 = tk.Entry(self.TabStrip1__Tab1,width=14,textvariable=ent2variable)
                    ent2.place(x=890, y=230)
                    ent2variable.set("1000.000")

                    ent3variable=tk.StringVar()
                    ent3 = tk.Entry(self.TabStrip1__Tab1,width=14,textvariable=ent3variable)
                    ent3.place(x=890, y=280)
                    ent3variable.set("595.000")
                    #标签
                    labsize2=font.Font(size=11,family="楷体")
                    ypzl=ttk.Label(self.TabStrip1__Tab1,text="油品种类：");ypzl.place(x=825,y=130)
                    zzl = ttk.Label(self.TabStrip1__Tab1, text="油罐直径(m)：");zzl.place(x=810, y=180)
                    ygzz = ttk.Label(self.TabStrip1__Tab1, text="油品周转量(m3)：");ygzz.place(x=790, y=230)
                    lost = ttk.Label(self.TabStrip1__Tab1, text="发油损耗量(kg)：");lost.place(x=790, y=280)
                    labypzl=ttk.Label(self.TabStrip1__Tab1,text="油品种类",font=labsize2);labypzl.place(x=25,y=27)
                    labzzl = ttk.Label(self.TabStrip1__Tab1, text="油品周转量(m3)", font=labsize2);labzzl.place(x=180, y=27)
                    labygzz = ttk.Label(self.TabStrip1__Tab1, text="油罐直径(m)", font=labsize2);labygzz.place(x=400, y=27)
                    lablost = ttk.Label(self.TabStrip1__Tab1, text="发油损耗量(kg)", font=labsize2);lablost.place(x=600, y=27)
                    #按钮
                    add=ttk.Button(self.TabStrip1__Tab1,text="   新增",command=addclick,width=8,image=from1.s31,compound="left")
                    add.place(x=850,y=320)
                    xiugai=ttk.Button(self.TabStrip1__Tab1, text="   计算",command=xiugaiclick,width=8,image=from1.s32,compound="left")
                    xiugai.place(x=850, y=360)
                    sanchu = ttk.Button(self.TabStrip1__Tab1, text="   删除",command=sanchuclick,width=8,image=from1.s33,compound="left")
                    sanchu.place(x=850, y=400)
                    sanchu = ttk.Button(self.TabStrip1__Tab1, text="   输出", command=printclick,width=8,image=from1.s34,compound="left")
                    sanchu.place(x=850, y=440)


                    self.TabStrip1__Tab2 = ttk.Frame(self.TabStrip1)
                    self.TabStrip1.add(self.TabStrip1__Tab2, text='无喷涂损耗',image=from1.s22,compound="left")
                    def fram2lbox2click(e2):
                        w2 = e2.widget
                        global t2
                        # 定义全局变量，可以用到下面的定义事件中
                        t2 = w2.curselection()
                        pass

                    def fram2addclick():
                        lbox2.insert(tk.END,
                                     "  " + youlei2.get() + "                                " +
                                     fram2ent1.get() + "                                               "
                        +fram2ent3.get() +

                                     "                                            " + fram2ent5.get())
                        pass

                    def fram2xiugaiclick():
                        pass

                    def fram2sanchuclick():
                        lbox2.delete(t8)
                        pass

                    def fram2printclick():
                        mesbox.showinfo('输出成功', '数据已输出成功，请在根目录下查看！')
                        i2 = 1
                        while i2 < 100:
                            result = str(lbox6.get(i2))
                            with open('无喷涂损耗计算损耗.text', 'a') as feil_handle:
                                feil_handle.write(result)
                                feil_handle.write("\n")
                            i2 += 1
                        pass

                        # 在如listbox控件

                    lbox2 = tk.Listbox(self.TabStrip1__Tab2, background="#89c291", height=28, width=105,
                                       font=('Arial', 10))
                    lbox2.place(x=18, y=65)
                    lbox2.bind("<<ListboxSelect>>", fram2lbox2click)

                    # 滚动条
                    scrollbar2 = ttk.Scrollbar(lbox2, command=lbox2.yview)
                    scrollbar2.place(x=718, y=0, height=480)
                    lbox2.config(yscrollcommand=scrollbar2.set)
                    scrollbar2.config(command=lbox2.yview)
                    # Adding a Combobox
                    youlei2 = tk.StringVar()
                    youlei2 = ttk.Combobox(self.TabStrip1__Tab2, width=11, textvariable=youlei2)
                    youlei2['values'] = ('石脑油', '汽  油', '柴  油', '煤  油', "蜡  油", "原  油")
                    youlei2.place(x=890, y=130)
                    youlei2.current(0)  # 设置初始显示值，值为元组['values']的下标
                    youlei2.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
                    # youlei.config(state='readonly')  # 设为只读模式
                    # 载入单行文本框
                    fram2ent1variable = tk.StringVar()
                    fram2ent1 = tk.Entry(self.TabStrip1__Tab2, width=14, textvariable=fram2ent1variable)
                    fram2ent1.place(x=890, y=180)
                    fram2ent1variable.set("1000.000")

                    fram2ent3variable = tk.StringVar()
                    fram2ent3 = tk.Entry(self.TabStrip1__Tab2, width=14, textvariable=fram2ent3variable)
                    fram2ent3.place(x=890, y=230)
                    fram2ent3variable.set("6.000")

                    fram2ent5variable = tk.StringVar()
                    fram2ent5 = tk.Entry(self.TabStrip1__Tab2, width=14, textvariable=fram2ent5variable)
                    fram2ent5.place(x=890, y=280)
                    fram2ent5variable.set("7.8867")
                    # 标签
                    fram2labsize2 = font.Font(size=11, family="楷体")
                    fram2ypzl = ttk.Label(self.TabStrip1__Tab2, text="油品种类：");
                    fram2ypzl.place(x=825, y=130)
                    fram2zqy = ttk.Label(self.TabStrip1__Tab2, text="油品周转量(m)：");
                    fram2zqy.place(x=795, y=180)
                    fram2zzl = ttk.Label(self.TabStrip1__Tab2, text="油罐直径(m):")
                    fram2zzl.place(x=810, y=230)
                    fram2lost = ttk.Label(self.TabStrip1__Tab2, text="发油损耗量(kg)：");
                    fram2lost.place(x=790, y=280)
                    fram2labypzl = ttk.Label(self.TabStrip1__Tab2, text="油品种类", font=fram2labsize2);
                    fram2labypzl.place(x=25, y=42)
                    fram2labzqy = ttk.Label(self.TabStrip1__Tab2, text="油品周转量(m3)", font=fram2labsize2);
                    fram2labzqy.place(x=180, y=42)
                    fram2labzzl = ttk.Label(self.TabStrip1__Tab2, text="油罐直径(m)", font=fram2labsize2);
                    fram2labzzl.place(x=400, y=42)
                    fram2lablost = ttk.Label(self.TabStrip1__Tab2, text="发油损耗量(kg)", font=fram2labsize2);
                    fram2lablost.place(x=600, y=42)
                    # 按钮
                    fram2add = ttk.Button(self.TabStrip1__Tab2, text="   新增", command=fram2addclick,width=8,image=from1.s31,compound="left");
                    fram2add.place(x=850, y=320)
                    fram2xiugai = ttk.Button(self.TabStrip1__Tab2, text="   计算", command=fram2xiugaiclick,width=8,image=from1.s32,compound="left");
                    fram2xiugai.place(x=850, y=360)
                    fram2sanchu = ttk.Button(self.TabStrip1__Tab2, text="   删除", command=fram2sanchuclick,width=8,image=from1.s33,compound="left");
                    fram2sanchu.place(x=850, y=400)
                    fram2sanchu = ttk.Button(self.TabStrip1__Tab2, text="   输出", command=fram2printclick,width=8,image=from1.s34,compound="left")
                    fram2sanchu.place(x=850, y=440)





                    self.TabStrip1__Tab3 = ttk.Frame(self.TabStrip1)
                    self.TabStrip1__Tab3Lbl = ttk.Label(self.TabStrip1__Tab3, text='Please add widgets in code.')
                    self.TabStrip1__Tab3Lbl.place(relx=0.1, rely=0.5)
                    self.TabStrip1.add(self.TabStrip1__Tab3, text='拱顶罐装油过程损耗',image=from1.s20,compound="left")
                    def fram3lbox3click(e3):
                        w3 = e3.widget
                        global t3
                        # 定义全局变量，可以用到下面的定义事件中
                        t3 = w3.curselection()
                        pass
                    def fram3addclick():
                        lbox3.insert(tk.END, "  "+youlei3.get()+"                           "
                                     +fram3ent1.get()+"                                   "+
                                     fram3ent2.get()+"                            "+fram3ent3.get()+
                                     "                        "+fram3ent4.get())
                        pass
                    def fram3xiugaiclick():
                        pass
                    def fram3sanchuclick():
                        lbox3.delete(t3)
                        pass
                    def fram3printclick():
                        mesbox.showinfo('输出成功', '数据已输出成功，请在根目录下查看！')
                        i3 = 1
                        while i3 < 100:
                            result = str(lbox2.get(i3))
                            with open('拱顶罐装油过程计算.text', 'a') as feil_handle:
                                feil_handle.write(result)
                                feil_handle.write("\n")
                            i3 += 1
                        pass

                    # 在如listbox控件
                    lbox3 = tk.Listbox(self.TabStrip1__Tab3, background="#89c291", height=28, width=105,
                                       font=('Arial', 10))
                    lbox3.place(x=18, y=65)
                    lbox3.bind("<<ListboxSelect>>", fram3lbox3click)

                    # 滚动条
                    scrollbar3 = ttk.Scrollbar(lbox3, command=lbox3.yview)
                    scrollbar3.place(x=718, y=0, height=480)
                    lbox3.config(yscrollcommand=scrollbar3.set)
                    scrollbar3.config(command=lbox3.yview)
                    # Adding a Combobox
                    youlei3 = tk.StringVar()
                    youlei3 = ttk.Combobox(self.TabStrip1__Tab3, width=11, textvariable=youlei3)
                    youlei3['values'] = ("原  油",'石脑油', '汽  油', '柴  油', '煤  油',"蜡  油")
                    youlei3.place(x=930,y=70)
                    youlei3.current(0)  # 设置初始显示值，值为元组['values']的下标
                    youlei3.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
                    # youlei.config(state='readonly')  # 设为只读模式
                    # 载入单行文本框
                    fram3ent1variable=tk.StringVar()
                    fram3ent1 = tk.Entry(self.TabStrip1__Tab3,width=14,textvariable=fram3ent1variable)
                    fram3ent1.place(x=930, y=120)
                    fram3ent1variable.set("10.000")

                    fram3ent2variable=tk.StringVar()
                    fram3ent2 = tk.Entry(self.TabStrip1__Tab3,width=14,textvariable=fram3ent2variable)
                    fram3ent2.place(x=930, y=170)
                    fram3ent2variable.set("1000.000")

                    fram3ent3variable=tk.StringVar()
                    fram3ent3 = tk.Entry(self.TabStrip1__Tab3,width=14,textvariable=fram3ent3variable)
                    fram3ent3.place(x=930, y=220)
                    fram3ent3variable.set("100.000")

                    fram3ent4variable = tk.StringVar()
                    fram3ent4 = tk.Entry(self.TabStrip1__Tab3, width=14, textvariable=fram3ent4variable)
                    fram3ent4.place(x=930, y=270)
                    fram3ent4variable.set("8.0090")
                    #标签
                    fram3labsize3=font.Font(size=11,family="楷体")
                    fram3ypzl=ttk.Label(self.TabStrip1__Tab3,text="油品种类：");fram3ypzl.place(x=865,y=70)
                    fram3zqy = ttk.Label(self.TabStrip1__Tab3, text="油品本体温度下蒸气压(Kpa)：");fram3zqy.place(x=760, y=120)
                    fram3ygzz = ttk.Label(self.TabStrip1__Tab3, text="油罐容积(m3)：");fram3ygzz.place(x=840, y=170)
                    fram3zzl = ttk.Label(self.TabStrip1__Tab3, text="油罐周转量(kg)：");fram3zzl.place(x=830, y=220)
                    fram3lost = ttk.Label(self.TabStrip1__Tab3, text="发油损耗量(kg)：");fram3lost.place(x=830, y=270)
                    fram3labypzl=ttk.Label(self.TabStrip1__Tab3,text="油品种类",font=fram3labsize3);fram3labypzl.place(x=18,y=42)
                    fram3labzqy = ttk.Label(self.TabStrip1__Tab3, text="油品本体温度下蒸气压(Kpa)", font=fram3labsize3);fram3labzqy.place(x=120, y=42)
                    fram3labygzz = ttk.Label(self.TabStrip1__Tab3, text="油罐容积(m3)", font=fram3labsize3);fram3labygzz.place(x=350, y=42)
                    fram3labzzl = ttk.Label(self.TabStrip1__Tab3, text="油罐周转量(kg)", font=fram3labsize3);fram3labzzl.place(x=470, y=42)
                    fram3lablost = ttk.Label(self.TabStrip1__Tab3, text="发油损耗量(kg)", font=fram3labsize3);fram3lablost.place(x=620, y=42)
                    #按钮
                    fram3add=ttk.Button(self.TabStrip1__Tab3,text="   新增",command=fram3addclick,width=8,image=from1.s31,compound="left")
                    fram3add.place(x=890,y=310)
                    fram3xiugai=ttk.Button(self.TabStrip1__Tab3, text="   计算",command=fram3xiugaiclick,width=8,image=from1.s32,compound="left")
                    fram3xiugai.place(x=890, y=340)
                    fram3sanchu = ttk.Button(self.TabStrip1__Tab3, text="   删除",command=fram3sanchuclick,width=8,image=from1.s33,compound="left")
                    fram3sanchu.place(x=890, y=370)
                    fram3sanchu = ttk.Button(self.TabStrip1__Tab3, text="   输出", command=fram3printclick,width=8,image=from1.s34,compound="left")
                    fram3sanchu.place(x=890, y=400)

                    self.TabStrip1__Tab4 = ttk.Frame(self.TabStrip1)
                    self.TabStrip1__Tab4Lbl = ttk.Label(self.TabStrip1__Tab4, text='Please add widgets in code.')
                    self.TabStrip1__Tab4Lbl.place(relx=0.1, rely=0.5)
                    self.TabStrip1.add(self.TabStrip1__Tab4, text='罐车未经清洗',image=from1.s18,compound="left")
                    def fram4lbox4click(e4):
                        w4= e4.widget
                        global t4
                        # 定义全局变量，可以用到下面的定义事件中
                        t4 = w4.curselection()
                        pass

                    def fram4addclick():
                        lbox4.insert(tk.END,
                                     "  " + youlei4.get() + "              " + fram4ent1.get() + "               " +
                                     fram4ent2.get() + "                           " + fram4ent3.get() +
                                     "                             " + fram4ent4.get()+
                                     "                          " + fram4ent5.get())
                        pass

                    def fram4xiugaiclick():
                        pass

                    def fram4sanchuclick():
                        lbox4.delete(t4)
                        pass

                    def fram4printclick():
                        mesbox.showinfo('输出成功', '数据已输出成功，请在根目录下查看！')
                        i4= 1
                        while i4 < 100:
                            result = str(lbox6.get(i4))
                            with open('罐车(未清洗)损耗计算.text', 'a') as feil_handle:
                                feil_handle.write(result)
                                feil_handle.write("\n")
                            i4 += 1
                        pass

                        # 在如listbox控件

                    lbox4 = tk.Listbox(self.TabStrip1__Tab4, background="#89c291", height=28, width=105,
                                       font=('Arial', 10))
                    lbox4.place(x=18, y=65)
                    lbox4.bind("<<ListboxSelect>>", fram4lbox4click)

                    # 滚动条
                    scrollbar4 = ttk.Scrollbar(lbox4, command=lbox4.yview)
                    scrollbar4.place(x=718, y=0, height=480)
                    lbox4.config(yscrollcommand=scrollbar4.set)
                    scrollbar4.config(command=lbox4.yview)
                    # Adding a Combobox
                    youlei4 = tk.StringVar()
                    youlei4 = ttk.Combobox(self.TabStrip1__Tab4, width=11, textvariable=youlei4)
                    youlei4['values'] = ('汽  油','石脑油',  '柴  油', '煤  油', "蜡  油", "原  油")
                    youlei4.place(x=915, y=70)
                    youlei4.current(0)  # 设置初始显示值，值为元组['values']的下标
                    youlei4.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
                    # youlei.config(state='readonly')  # 设为只读模式
                    # 载入单行文本框
                    fram4ent1variable = tk.StringVar()
                    fram4ent1 = tk.Entry(self.TabStrip1__Tab4, width=14, textvariable=fram4ent1variable)
                    fram4ent1.place(x=915, y=120)
                    fram4ent1variable.set("0.309")

                    fram4ent2variable = tk.StringVar()
                    fram4ent2 = tk.Entry(self.TabStrip1__Tab4, width=14, textvariable=fram4ent2variable)
                    fram4ent2.place(x=915, y=170)
                    fram4ent2variable.set("0.785")

                    fram4ent3variable = tk.StringVar()
                    fram4ent3 = tk.Entry(self.TabStrip1__Tab4, width=14, textvariable=fram4ent3variable)
                    fram4ent3.place(x=915, y=220)
                    fram4ent3variable.set("0.500")

                    fram4ent4variable = tk.StringVar()
                    fram4ent4 = tk.Entry(self.TabStrip1__Tab4, width=14, textvariable=fram4ent4variable)
                    fram4ent4.place(x=915, y=270)
                    fram4ent4variable.set("1000.000")

                    fram4ent5variable = tk.StringVar()
                    fram4ent5 = tk.Entry(self.TabStrip1__Tab4, width=14, textvariable=fram4ent5variable)
                    fram4ent5.place(x=915, y=320)
                    fram4ent5variable.set("525.000")
                    # 标签
                    fram4labsize4 = font.Font(size=11, family="楷体")
                    fram4ypzl = ttk.Label(self.TabStrip1__Tab4, text="油品种类：");
                    fram4ypzl.place(x=850, y=70)
                    fram4zqy = ttk.Label(self.TabStrip1__Tab4, text="浓度下限：");
                    fram4zqy.place(x=850, y=120)
                    fram4ygzz = ttk.Label(self.TabStrip1__Tab4, text="浓度上限：");
                    fram4ygzz.place(x=850, y=170)
                    fram4zzl = ttk.Label(self.TabStrip1__Tab4, text="气体浓度(夏高冬低kg/m3):")
                    fram4zzl.place(x=760, y=220)
                    fram4zytj = ttk.Label(self.TabStrip1__Tab4, text="装油体积(m3)：")
                    fram4zytj.place(x=824, y=270)
                    fram4lost = ttk.Label(self.TabStrip1__Tab4, text="罐车(未清洗)损耗量(kg)：");
                    fram4lost.place(x=770, y=320)
                    fram4labypzl = ttk.Label(self.TabStrip1__Tab4, text="油品种类", font=fram4labsize4);
                    fram4labypzl.place(x=18, y=42)
                    fram4labzqy = ttk.Label(self.TabStrip1__Tab4, text="浓度下限", font=fram4labsize4);
                    fram4labzqy.place(x=100, y=42)
                    fram4labygzz = ttk.Label(self.TabStrip1__Tab4, text="浓度上限", font=fram4labsize4);
                    fram4labygzz.place(x=180, y=42)
                    fram4labzzl = ttk.Label(self.TabStrip1__Tab4, text="气体浓度(夏高冬低kg/m3)", font=fram4labsize4);
                    fram4labzzl.place(x=270, y=42)
                    fram4labzytj = ttk.Label(self.TabStrip1__Tab4, text="装油体积(m3)", font=fram4labsize4);
                    fram4labzytj.place(x=480, y=42)
                    fram4lablost = ttk.Label(self.TabStrip1__Tab4, text="罐车(未清洗)损耗量(kg)", font=fram4labsize4);
                    fram4lablost.place(x=600, y=42)
                    # 按钮
                    fram4add = ttk.Button(self.TabStrip1__Tab4, text="   新增", command=fram4addclick,width=8,image=from1.s31,compound="left")
                    fram4add.place(x=900, y=360)
                    fram4xiugai = ttk.Button(self.TabStrip1__Tab4, text="   计算", command=fram4xiugaiclick,width=8,image=from1.s32,compound="left");
                    fram4xiugai.place(x=900, y=395)
                    fram4sanchu = ttk.Button(self.TabStrip1__Tab4, text="   删除", command=fram4sanchuclick,width=8,image=from1.s33,compound="left");
                    fram4sanchu.place(x=900, y=430)
                    fram4sanchu = ttk.Button(self.TabStrip1__Tab4, text="   输出", command=fram4printclick,width=8,image=from1.s34,compound="left")
                    fram4sanchu.place(x=900, y=465)

                    self.TabStrip1__Tab5 = ttk.Frame(self.TabStrip1)
                    self.TabStrip1__Tab5Lbl = ttk.Label(self.TabStrip1__Tab5, text='Please add widgets in code.')
                    self.TabStrip1__Tab5Lbl.place(relx=0.1, rely=0.5)
                    self.TabStrip1.add(self.TabStrip1__Tab5, text='罐车经过清洗',image=from1.s17,compound="left")

                    def fram5lbox5click(e5):
                        w5= e5.widget
                        global t5
                        # 定义全局变量，可以用到下面的定义事件中
                        t5 = w5.curselection()
                        pass

                    def fram5addclick():
                        lbox5.insert(tk.END,
                                     "  " + youlei5.get() + "              " + fram5ent1.get() + "               " +
                                     fram5ent2.get() + "                           " + fram5ent3.get() +
                                     "                             " + fram5ent4.get()+
                                     "                          " + fram5ent5.get())
                        pass

                    def fram5xiugaiclick():
                        pass

                    def fram5sanchuclick():
                        lbox5.delete(t5)
                        pass

                    def fram5printclick():
                        mesbox.showinfo('输出成功', '数据已输出成功，请在根目录下查看！')
                        i5= 1
                        while i5 < 100:
                            result = str(lbox6.get(i5))
                            with open('罐车(未清洗)损耗计算.text', 'a') as feil_handle:
                                feil_handle.write(result)
                                feil_handle.write("\n")
                            i5 += 1
                        pass

                        # 在如listbox控件

                    lbox5 = tk.Listbox(self.TabStrip1__Tab5, background="#89c291", height=28, width=105,
                                       font=('Arial', 10))
                    lbox5.place(x=18, y=65)
                    lbox5.bind("<<ListboxSelect>>", fram4lbox4click)

                    # 滚动条
                    scrollbar5 = ttk.Scrollbar(lbox5, command=lbox5.yview)
                    scrollbar5.place(x=718, y=0, height=480)
                    lbox5.config(yscrollcommand=scrollbar4.set)
                    scrollbar4.config(command=lbox5.yview)
                    # Adding a Combobox
                    youlei5 = tk.StringVar()
                    youlei5 = ttk.Combobox(self.TabStrip1__Tab5, width=11, textvariable=youlei5)
                    youlei5['values'] = ('汽  油','石脑油',  '柴  油', '煤  油', "蜡  油", "原  油")
                    youlei5.place(x=915, y=70)
                    youlei5.current(0)  # 设置初始显示值，值为元组['values']的下标
                    youlei5.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
                    # youlei.config(state='readonly')  # 设为只读模式
                    # 载入单行文本框
                    fram5ent1variable = tk.StringVar()
                    fram5ent1 = tk.Entry(self.TabStrip1__Tab5, width=14, textvariable=fram5ent1variable)
                    fram5ent1.place(x=915, y=120)
                    fram5ent1variable.set("0.309")

                    fram5ent2variable = tk.StringVar()
                    fram5ent2 = tk.Entry(self.TabStrip1__Tab5, width=14, textvariable=fram5ent2variable)
                    fram5ent2.place(x=915, y=170)
                    fram5ent2variable.set("0.785")

                    fram5ent3variable = tk.StringVar()
                    fram5ent3 = tk.Entry(self.TabStrip1__Tab5, width=14, textvariable=fram5ent3variable)
                    fram5ent3.place(x=915, y=220)
                    fram5ent3variable.set("0.500")

                    fram5ent4variable = tk.StringVar()
                    fram5ent4 = tk.Entry(self.TabStrip1__Tab5, width=14, textvariable=fram5ent4variable)
                    fram5ent4.place(x=915, y=270)
                    fram5ent4variable.set("1000.000")

                    fram5ent5variable = tk.StringVar()
                    fram5ent5 = tk.Entry(self.TabStrip1__Tab5, width=14, textvariable=fram5ent5variable)
                    fram5ent5.place(x=915, y=320)
                    fram5ent5variable.set("525.000")
                    # 标签
                    fram5labsize5 = font.Font(size=11, family="楷体")
                    fram5ypzl = ttk.Label(self.TabStrip1__Tab5, text="油品种类：");
                    fram5ypzl.place(x=850, y=70)
                    fram5zqy = ttk.Label(self.TabStrip1__Tab5, text="浓度下限：");
                    fram5zqy.place(x=850, y=120)
                    fram5ygzz = ttk.Label(self.TabStrip1__Tab5, text="浓度上限：");
                    fram5ygzz.place(x=850, y=170)
                    fram5zzl = ttk.Label(self.TabStrip1__Tab5, text="气体浓度(夏高冬低kg/m3):")
                    fram5zzl.place(x=760, y=220)
                    fram5zytj = ttk.Label(self.TabStrip1__Tab5, text="装油体积(m3)：")
                    fram5zytj.place(x=824, y=270)
                    fram5lost = ttk.Label(self.TabStrip1__Tab5, text="罐车(清洗)损耗量(kg)：");
                    fram5lost.place(x=780, y=320)
                    fram5labypzl = ttk.Label(self.TabStrip1__Tab5, text="油品种类", font=fram5labsize5);
                    fram5labypzl.place(x=18, y=42)
                    fram5labzqy = ttk.Label(self.TabStrip1__Tab5, text="浓度下限", font=fram5labsize5);
                    fram5labzqy.place(x=100, y=42)
                    fram5labygzz = ttk.Label(self.TabStrip1__Tab5, text="浓度上限", font=fram5labsize5);
                    fram5labygzz.place(x=180, y=42)
                    fram5labzzl = ttk.Label(self.TabStrip1__Tab5, text="气体浓度(夏高冬低kg/m3)", font=fram5labsize5);
                    fram5labzzl.place(x=270, y=42)
                    fram5labzytj = ttk.Label(self.TabStrip1__Tab5, text="装油体积(m3)", font=fram5labsize5);
                    fram5labzytj.place(x=480, y=42)
                    fram5lablost = ttk.Label(self.TabStrip1__Tab5, text="罐车(清洗)损耗量(kg)", font=fram5labsize5);
                    fram5lablost.place(x=605, y=42)
                    # 按钮
                    fram5add = ttk.Button(self.TabStrip1__Tab5, text="   新增", command=fram5addclick,width=8,image=from1.s31,compound="left");
                    fram5add.place(x=900, y=360)
                    fram5xiugai = ttk.Button(self.TabStrip1__Tab5, text="   计算", command=fram5xiugaiclick,width=8,image=from1.s32,compound="left");
                    fram5xiugai.place(x=900, y=395)
                    fram5sanchu = ttk.Button(self.TabStrip1__Tab5, text="   删除", command=fram5sanchuclick,width=8,image=from1.s33,compound="left");
                    fram5sanchu.place(x=900, y=430)
                    fram5sanchu = ttk.Button(self.TabStrip1__Tab5, text="   输出", command=fram5printclick,width=8,image=from1.s34,compound="left")
                    fram5sanchu.place(x=900, y=465)

                    self.TabStrip1__Tab6 = ttk.Frame(self.TabStrip1)
                    self.TabStrip1.add(self.TabStrip1__Tab6, text='船装损耗',image=from1.s16,compound="left")
                    def fram6lbox6click(e6):
                        w6 = e6.widget
                        global t6
                        # 定义全局变量，可以用到下面的定义事件中
                        t6 = w6.curselection()
                        pass

                    def fram6addclick():
                        lbox6.insert(tk.END,
                                     "  " + youlei6.get() + "              " + fram6ent1.get() + "               " +
                                     fram6ent2.get() + "                           " + fram6ent3.get() +
                                     "                             " + fram6ent4.get()+
                                     "                          " + fram6ent5.get())
                        pass

                    def fram6xiugaiclick():
                        pass

                    def fram6sanchuclick():
                        lbox6.delete(t6)
                        pass

                    def fram6printclick():
                        mesbox.showinfo('输出成功', '数据已输出成功，请在根目录下查看！')
                        i6 = 1
                        while i6 < 100:
                            result = str(lbox6.get(i6))
                            with open('船装损耗计算.text', 'a') as feil_handle:
                                feil_handle.write(result)
                                feil_handle.write("\n")
                            i6 += 1
                        pass

                        # 在如listbox控件

                    lbox6 = tk.Listbox(self.TabStrip1__Tab6, background="#89c291", height=28, width=105,
                                       font=('Arial', 10))
                    lbox6.place(x=18, y=65)
                    lbox6.bind("<<ListboxSelect>>", fram6lbox6click)

                    # 滚动条
                    scrollbar6 = ttk.Scrollbar(lbox6, command=lbox6.yview)
                    scrollbar6.place(x=718, y=0, height=480)
                    lbox6.config(yscrollcommand=scrollbar6.set)
                    scrollbar6.config(command=lbox6.yview)
                    # Adding a Combobox
                    youlei6 = tk.StringVar()
                    youlei6 = ttk.Combobox(self.TabStrip1__Tab6, width=11, textvariable=youlei6)
                    youlei6['values'] = ('汽  油','石脑油',  '柴  油', '煤  油', "蜡  油", "原  油")
                    youlei6.place(x=915, y=70)
                    youlei6.current(0)  # 设置初始显示值，值为元组['values']的下标
                    youlei6.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
                    # youlei.config(state='readonly')  # 设为只读模式
                    # 载入单行文本框
                    fram6ent1variable = tk.StringVar()
                    fram6ent1 = tk.Entry(self.TabStrip1__Tab6, width=14, textvariable=fram6ent1variable)
                    fram6ent1.place(x=915, y=120)
                    fram6ent1variable.set("0.309")

                    fram6ent2variable = tk.StringVar()
                    fram6ent2 = tk.Entry(self.TabStrip1__Tab6, width=14, textvariable=fram6ent2variable)
                    fram6ent2.place(x=915, y=170)
                    fram6ent2variable.set("0.785")

                    fram6ent3variable = tk.StringVar()
                    fram6ent3 = tk.Entry(self.TabStrip1__Tab6, width=14, textvariable=fram6ent3variable)
                    fram6ent3.place(x=915, y=220)
                    fram6ent3variable.set("0.500")

                    fram6ent4variable = tk.StringVar()
                    fram6ent4 = tk.Entry(self.TabStrip1__Tab6, width=14, textvariable=fram6ent4variable)
                    fram6ent4.place(x=915, y=270)
                    fram6ent4variable.set("1000.000")

                    fram6ent5variable = tk.StringVar()
                    fram6ent5 = tk.Entry(self.TabStrip1__Tab6, width=14, textvariable=fram6ent5variable)
                    fram6ent5.place(x=915, y=320)
                    fram6ent5variable.set("525.000")
                    # 标签
                    fram6labsize6 = font.Font(size=11, family="楷体")
                    fram6ypzl = ttk.Label(self.TabStrip1__Tab6, text="油品种类：");
                    fram6ypzl.place(x=850, y=70)
                    fram6zqy = ttk.Label(self.TabStrip1__Tab6, text="浓度下限：");
                    fram6zqy.place(x=850, y=120)
                    fram6ygzz = ttk.Label(self.TabStrip1__Tab6, text="浓度上限：");
                    fram6ygzz.place(x=850, y=170)
                    fram6zzl = ttk.Label(self.TabStrip1__Tab6, text="气体浓度(夏高冬低kg/m3):")
                    fram6zzl.place(x=760, y=220)
                    fram6zytj = ttk.Label(self.TabStrip1__Tab6, text="装油体积(m3)：")
                    fram6zytj.place(x=824, y=270)
                    fram6lost = ttk.Label(self.TabStrip1__Tab6, text="船装损耗量(kg)：");
                    fram6lost.place(x=814, y=320)
                    fram6labypzl = ttk.Label(self.TabStrip1__Tab6, text="油品种类", font=fram6labsize6);
                    fram6labypzl.place(x=18, y=42)
                    fram6labzqy = ttk.Label(self.TabStrip1__Tab6, text="浓度下限", font=fram6labsize6);
                    fram6labzqy.place(x=100, y=42)
                    fram6labygzz = ttk.Label(self.TabStrip1__Tab6, text="浓度上限", font=fram6labsize6);
                    fram6labygzz.place(x=180, y=42)
                    fram6labzzl = ttk.Label(self.TabStrip1__Tab6, text="气体浓度(夏高冬低kg/m3)", font=fram6labsize6);
                    fram6labzzl.place(x=270, y=42)
                    fram6labzytj = ttk.Label(self.TabStrip1__Tab6, text="装油体积(m3)", font=fram6labsize6);
                    fram6labzytj.place(x=480, y=42)
                    fram6lablost = ttk.Label(self.TabStrip1__Tab6, text="船装损耗量(kg)", font=fram6labsize6);
                    fram6lablost.place(x=600, y=42)
                    # 按钮
                    fram6add = ttk.Button(self.TabStrip1__Tab6, text="   新增", command=fram6addclick,width=8,image=from1.s31,compound="left");
                    fram6add.place(x=900, y=360)
                    fram6xiugai = ttk.Button(self.TabStrip1__Tab6, text="   计算", command=fram6xiugaiclick,width=8,image=from1.s32,compound="left");
                    fram6xiugai.place(x=900, y=395)
                    fram6sanchu = ttk.Button(self.TabStrip1__Tab6, text="   删除", command=fram6sanchuclick,width=8,image=from1.s33,compound="left");
                    fram6sanchu.place(x=900, y=430)
                    fram6sanchu = ttk.Button(self.TabStrip1__Tab6, text="   输出", command=fram6printclick,width=8,image=from1.s34,compound="left")
                    fram6sanchu.place(x=900, y=465)

                    self.TabStrip1__Tab7 = ttk.Frame(self.TabStrip1)
                    self.TabStrip1.add(self.TabStrip1__Tab7, text='静储损耗',image=from1.s15,compound="left")
                    def fram7lbox7click(e7):
                        w7 = e7.widget
                        global t7
                        # 定义全局变量，可以用到下面的定义事件中
                        t7 = w7.curselection()
                        pass

                    def fram7addclick():
                        lbox7.insert(tk.END,
                                     "  " + youlei7.get() + "       " + fram7ent1.get() + "                        " +
                                     fram7ent2.get() + "                                " + fram7ent3.get() +
                                     "                         " + fram7ent4.get()+
                                     "                             " + fram7ent5.get())
                        pass

                    def fram7xiugaiclick():
                        pass

                    def fram7sanchuclick():
                        lbox7.delete(t7)
                        pass

                    def fram7printclick():
                        mesbox.showinfo('输出成功', '数据已输出成功，请在根目录下查看！')
                        i7 = 1
                        while i7 < 100:
                            result = str(lbox6.get(i7))
                            with open('静储损耗计算.text', 'a') as feil_handle:
                                feil_handle.write(result)
                                feil_handle.write("\n")
                            i7 += 1
                        pass

                        # 在如listbox控件

                    lbox7 = tk.Listbox(self.TabStrip1__Tab7, background="#89c291", height=28, width=105,
                                       font=('Arial', 10))
                    lbox7.place(x=18, y=65)
                    lbox7.bind("<<ListboxSelect>>", fram7lbox7click)

                    # 滚动条
                    scrollbar7 = ttk.Scrollbar(lbox7, command=lbox7.yview)
                    scrollbar7.place(x=718, y=0, height=480)
                    lbox7.config(yscrollcommand=scrollbar7.set)
                    scrollbar7.config(command=lbox7.yview)
                    # Adding a Combobox
                    youlei7 = tk.StringVar()
                    youlei7 = ttk.Combobox(self.TabStrip1__Tab7, width=11, textvariable=youlei7)
                    youlei7['values'] = ('石脑油', '汽  油', '柴  油', '煤  油', "蜡  油", "原  油")
                    youlei7.place(x=920, y=70)
                    youlei7.current(0)  # 设置初始显示值，值为元组['values']的下标
                    youlei7.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
                    # youlei.config(state='readonly')  # 设为只读模式
                    # 载入单行文本框
                    fram7ent1variable = tk.StringVar()
                    fram7ent1 = tk.Entry(self.TabStrip1__Tab7, width=14, textvariable=fram7ent1variable)
                    fram7ent1.place(x=920, y=120)
                    fram7ent1variable.set("100.000")

                    fram7ent2variable = tk.StringVar()
                    fram7ent2 = tk.Entry(self.TabStrip1__Tab7, width=14, textvariable=fram7ent2variable)
                    fram7ent2.place(x=920, y=170)
                    fram7ent2variable.set("2.000")

                    fram7ent3variable = tk.StringVar()
                    fram7ent3 = tk.Entry(self.TabStrip1__Tab7, width=14, textvariable=fram7ent3variable)
                    fram7ent3.place(x=920, y=220)
                    fram7ent3variable.set("5.000")

                    fram7ent4variable = tk.StringVar()
                    fram7ent4 = tk.Entry(self.TabStrip1__Tab7, width=14, textvariable=fram7ent4variable)
                    fram7ent4.place(x=920, y=270)
                    fram7ent4variable.set("4.000")

                    fram7ent5variable = tk.StringVar()
                    fram7ent5 = tk.Entry(self.TabStrip1__Tab7, width=14, textvariable=fram6ent5variable)
                    fram7ent5.place(x=920, y=320)
                    fram7ent5variable.set("0.0022")
                    # 标签
                    fram7labsize7 = font.Font(size=11, family="楷体")
                    fram7ypzl = ttk.Label(self.TabStrip1__Tab7, text="油品种类：");
                    fram7ypzl.place(x=855, y=70)
                    fram7zqy = ttk.Label(self.TabStrip1__Tab7, text="油罐直径(m)：");
                    fram7zqy.place(x=840, y=120)
                    fram7ygzz = ttk.Label(self.TabStrip1__Tab7, text="平均油温下真实蒸气压(Kpa):");
                    fram7ygzz.place(x=760, y=170)
                    fram7zzl = ttk.Label(self.TabStrip1__Tab7, text="静储时间(h):")
                    fram7zzl.place(x=846, y=220)
                    fram7zytj = ttk.Label(self.TabStrip1__Tab7, text="油罐所在地平均风速(m/s)：")
                    fram7zytj.place(x=765, y=270)
                    fram7lost = ttk.Label(self.TabStrip1__Tab7, text="静储存损耗量：");
                    fram7lost.place(x=831, y=320)
                    fram7labypzl = ttk.Label(self.TabStrip1__Tab7, text="油品种类", font=fram7labsize7);
                    fram7labypzl.place(x=14, y=42)
                    fram7labzqy = ttk.Label(self.TabStrip1__Tab7, text="油罐直径", font=fram7labsize7);
                    fram7labzqy.place(x=90, y=42)
                    fram7labygzz = ttk.Label(self.TabStrip1__Tab7, text="平均油温下真实蒸气压(Kpa)", font=fram7labsize7);
                    fram7labygzz.place(x=160, y=42)
                    fram7labzzl = ttk.Label(self.TabStrip1__Tab7, text="静储时间(h)", font=fram7labsize7);
                    fram7labzzl.place(x=370, y=42)
                    fram7labzytj = ttk.Label(self.TabStrip1__Tab7, text="油罐所在地平均风速(m/s)", font=fram7labsize7);
                    fram7labzytj.place(x=470, y=42)
                    fram7lablost = ttk.Label(self.TabStrip1__Tab7, text="静储存损耗量(kg)", font=fram7labsize7);
                    fram7lablost.place(x=660, y=42)
                    # 按钮
                    fram7add = ttk.Button(self.TabStrip1__Tab7, text="   新增", command=fram7addclick,width=8,image=from1.s31,compound="left");
                    fram7add.place(x=900, y=360)
                    fram7xiugai = ttk.Button(self.TabStrip1__Tab7, text="   计算", command=fram7xiugaiclick,width=8,image=from1.s32,compound="left");
                    fram7xiugai.place(x=900, y=395)
                    fram7sanchu = ttk.Button(self.TabStrip1__Tab7, text="   删除", command=fram7sanchuclick,width=8,image=from1.s33,compound="left");
                    fram7sanchu.place(x=900, y=430)
                    fram7sanchu = ttk.Button(self.TabStrip1__Tab7, text="   输出", command=fram7printclick,width=8,image=from1.s34,compound="left")
                    fram7sanchu.place(x=900, y=465)


                    self.TabStrip1__Tab8 = ttk.Frame(self.TabStrip1)
                    # self.TabStrip1__Tab8Lbl = ttk.Label(self.TabStrip1__Tab6, text='Please add widgets in code.')
                    # self.TabStrip1__Tab8Lbl.place(relx=0.1, rely=0.5)
                    self.TabStrip1.add(self.TabStrip1__Tab8, text='输储（无喷涂内衬）损耗',image=from1.s21,compound="left")
                    def fram8lbox8click(e8):
                        w8 = e8.widget
                        global t8
                        # 定义全局变量，可以用到下面的定义事件中
                        t8 = w8.curselection()
                        pass

                    def fram8addclick():
                        lbox8.insert(tk.END,
                                     "  " + youlei8.get() + "                                " +
                                     fram8ent1.get() + "                                               "
                        +fram8ent3.get() +

                                     "                                            " + fram8ent5.get())
                        pass

                    def fram8xiugaiclick():
                        pass

                    def fram8sanchuclick():
                        lbox8.delete(t8)
                        pass

                    def fram8printclick():
                        mesbox.showinfo('输出成功', '数据已输出成功，请在根目录下查看！')
                        i8 = 1
                        while i8 < 100:
                            result = str(lbox6.get(i8))
                            with open('输储(内壁无喷涂内衬)损耗.text', 'a') as feil_handle:
                                feil_handle.write(result)
                                feil_handle.write("\n")
                            i8 += 1
                        pass

                        # 在如listbox控件

                    lbox8 = tk.Listbox(self.TabStrip1__Tab8, background="#89c291", height=28, width=105,
                                       font=('Arial', 10))
                    lbox8.place(x=18, y=65)
                    lbox8.bind("<<ListboxSelect>>", fram8lbox8click)

                    # 滚动条
                    scrollbar8 = ttk.Scrollbar(lbox8, command=lbox8.yview)
                    scrollbar8.place(x=718, y=0, height=480)
                    lbox8.config(yscrollcommand=scrollbar8.set)
                    scrollbar8.config(command=lbox8.yview)
                    # Adding a Combobox
                    youlei8 = tk.StringVar()
                    youlei8 = ttk.Combobox(self.TabStrip1__Tab8, width=11, textvariable=youlei8)
                    youlei8['values'] = ('石脑油', '汽  油', '柴 油', '煤 油', "蜡  油", "原  油")
                    youlei8.place(x=890, y=130)
                    youlei8.current(0)  # 设置初始显示值，值为元组['values']的下标
                    youlei8.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
                    # youlei.config(state='readonly')  # 设为只读模式
                    # 载入单行文本框
                    fram8ent1variable = tk.StringVar()
                    fram8ent1 = tk.Entry(self.TabStrip1__Tab8, width=14, textvariable=fram8ent1variable)
                    fram8ent1.place(x=890, y=190)
                    fram8ent1variable.set("1000.000")

                    fram8ent3variable = tk.StringVar()
                    fram8ent3 = tk.Entry(self.TabStrip1__Tab8, width=14, textvariable=fram8ent3variable)
                    fram8ent3.place(x=890, y=230)
                    fram8ent3variable.set("6.000")

                    fram8ent5variable = tk.StringVar()
                    fram8ent5 = tk.Entry(self.TabStrip1__Tab8, width=14, textvariable=fram8ent5variable)
                    fram8ent5.place(x=890, y=280)
                    fram8ent5variable.set("7.8867")
                    # 标签
                    fram8labsize8 = font.Font(size=11, family="楷体")
                    fram8ypzl = ttk.Label(self.TabStrip1__Tab8, text="油品种类：");
                    fram8ypzl.place(x=825, y=130)
                    fram8zqy = ttk.Label(self.TabStrip1__Tab8, text="油品周转量(m)：");
                    fram8zqy.place(x=795, y=180)
                    fram8zzl = ttk.Label(self.TabStrip1__Tab8, text="油罐直径(m):")
                    fram8zzl.place(x=810, y=230)
                    fram8lost = ttk.Label(self.TabStrip1__Tab8, text="发油损耗量(kg)：");
                    fram8lost.place(x=790, y=280)
                    fram8labypzl = ttk.Label(self.TabStrip1__Tab8, text="油品种类", font=fram8labsize8);
                    fram8labypzl.place(x=25, y=42)
                    fram8labzqy = ttk.Label(self.TabStrip1__Tab8, text="油品周转量(m)", font=fram8labsize8);
                    fram8labzqy.place(x=180, y=42)
                    fram8labzzl = ttk.Label(self.TabStrip1__Tab8, text="油罐直径(m)", font=fram8labsize8);
                    fram8labzzl.place(x=400, y=42)
                    fram8lablost = ttk.Label(self.TabStrip1__Tab8, text="发油损耗量(kg)", font=fram8labsize8);
                    fram8lablost.place(x=600, y=42)
                    # 按钮
                    fram8add = ttk.Button(self.TabStrip1__Tab8, text="   新增", command=fram8addclick,width=8,image=from1.s31,compound="left");
                    fram8add.place(x=850, y=320)
                    fram8xiugai = ttk.Button(self.TabStrip1__Tab8, text="   计算", command=fram8xiugaiclick,width=8,image=from1.s32,compound="left");
                    fram8xiugai.place(x=850, y=360)
                    fram8sanchu = ttk.Button(self.TabStrip1__Tab8, text="   删除", command=fram8sanchuclick,width=8,image=from1.s33,compound="left");
                    fram8sanchu.place(x=850, y=400)
                    fram8sanchu = ttk.Button(self.TabStrip1__Tab8, text="   输出", command=fram8printclick,width=8,image=from1.s34,compound="left")
                    fram8sanchu.place(x=850, y=440)

                    #加载主页图片以及时间
                    fram0text1 = tk.Text(self.TabStrip1__Tab0, width=250, height=70)
                    fram0text1.place(x=1, y=1)
                    # 加载图片
                    fram0pic0 = Image.open("./img/bb.jpg")
                    # 定义照片大小
                    w, h = fram0pic0.size
                    fram0pic0 = fram0pic0.resize((int( 1.1* w), int(1.15* h)))
                    fram0pho0 = ImageTk.PhotoImage(fram0pic0)
                    fram0text1.image_create(tk.END, image=fram0pho0)

                    # selftext1 = tk.Text(self.master, width=16, height=44,background="#f0f0f0")
                    # selftext1.place(x=1045, y=30)
                    # # 加载图片
                    # selfpic0 = Image.open("./img/L1.png")
                    # # 定义照片大小
                    # w, h = selfpic0.size
                    # selfpic0 = selfpic0.resize((int(0.6* w), int(0.5* h)))
                    # selfpho0 = ImageTk.PhotoImage(selfpic0)
                    # selftext1.image_create(tk.END, image=selfpho0)

                    # selftext2 = tk.Text(self.master, width=20, height=20, background="#f0f0f0")
                    # selftext2.place(x=700, y=600)
                    # # 加载图片
                    # selfpic2 = Image.open("./img/s1.png")
                    # # 定义照片大小
                    # w, h = selfpic2.size
                    # selfpic2 = selfpic0.resize((int(0.5* w), int(0.5 * h)))
                    # selfpho2 = ImageTk.PhotoImage(selfpic2)
                    # selftext2.image_create(tk.END, image=selfpho2)

                    # 弹出框
                    def zhongleiclick():
                        from2 = tk.Tk()
                        from2.title("油品气体浓度范围")

                        # from2.geometry("800x600")
                        columns = ("运输形式", "油品种类", "浓度下限", "浓度上限")
                        treeview = ttk.Treeview(from2, height=18, show="headings", columns=columns)  # 表格

                        treeview.column("运输形式", width=180, anchor='center')  # 表示列,不显示
                        treeview.column("油品种类", width=150, anchor='center')
                        treeview.column("浓度下限", width=200, anchor='center')  # 表示列,不显示
                        treeview.column("浓度上限", width=200, anchor='center')

                        treeview.heading("运输形式", text="运输形式")  # 显示表头
                        treeview.heading("油品种类", text="油品种类")
                        treeview.heading("浓度下限", text="浓度下限")  # 显示表头
                        treeview.heading("浓度上限", text="浓度上限")

                        treeview.pack(side=tk.LEFT, fill=tk.BOTH)

                        ysxs = ['铁路罐装未清洗', '铁路罐未装清洗', '铁路罐装清洗']
                        # name=[entry1.get()]
                        ypzl = ['石脑油', '煤油', '石脑油']
                        xx = ['0.4090', '0.0870', '0.3040']
                        sx = ['0.8840', '0.1190', '0.8640']
                        for i in range(min(len(ysxs), len(ypzl), len(xx), len(sx))):  # 写入数据
                            treeview.insert('', i, values=(ysxs[i], ypzl[i], xx[i], sx[i]))

                        def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
                            l = [(tv.set(k, col), k) for k in tv.get_children('')]
                            l.sort(reverse=reverse)  # 排序方式
                            # rearrange items in sorted positions
                            for index, (val, k) in enumerate(l):  # 根据排序后索引移动
                                tv.move(k, '', index)
                            tv.heading(col,
                                       command=lambda: treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

                        def set_cell_value(event):  # 双击进入编辑状态
                            for item in treeview.selection():
                                # item = I001
                                item_text = treeview.item(item, "values")
                                # print(item_text[0:4])  # 输出所选行的值
                            column = treeview.identify_column(event.x)  # 列
                            row = treeview.identify_row(event.y)  # 行
                            cn = int(str(column).replace('#', ''))
                            rn = int(str(row).replace('I', ''))
                            entryedit = tk.Text(from2, width=10 + (cn - 1) * 4, height=1)
                            entryedit.place(x=16 + (cn - 1) * 180, y=6 + rn * 20)

                            def saveedit():
                                treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
                                entryedit.destroy()
                                okb.destroy()

                            okb = ttk.Button(from2, text='OK', width=4, command=saveedit)
                            okb.place(x=90 + (cn - 1) * 205, y=2 + rn * 20)

                        def newrow():
                            ysxs.append('请输入运输形式')
                            ypzl.append('请输入油品')
                            xx.append("请输入浓度下限")
                            sx.append("请输入浓度上限")
                            treeview.insert('', len(ysxs) - 1, values=(ysxs[len(ysxs) - 1], ypzl[len(ysxs) - 1],
                                                                       xx[len(ysxs) - 1], sx[(len(ysxs) - 1)])
                                            )
                            treeview.update()
                            newb.place(x=280, y=(len(ysxs) - 1) * 20 + 45)
                            newb.update()

                        treeview.bind('<Double-1>', set_cell_value)  # 双击左键进入编辑
                        newb = ttk.Button(from2, text='新增', width=10, command=newrow)
                        newb.place(x=280, y=(len(ysxs) - 1) * 20 + 45)

                        for col in columns:  # 绑定函数，使表头可排序
                            treeview.heading(col, text=col,
                                             command=lambda _col=col: treeview_sort_column(treeview, _col, False))


                        from2.mainloop()
                        pass


                    def youpinclick():
                        from8 = tk.Tk()  # 初始框的声明
                        from8.title("油品种类")
                        columns = ("油品编号", "油品名称")
                        treeview = ttk.Treeview(from8, height=18, show="headings", columns=columns)  # 表格

                        treeview.column("油品编号", width=100, anchor='center')  # 表示列,不显示
                        treeview.column("油品名称", width=300, anchor='center')

                        treeview.heading("油品编号", text="油品编号")  # 显示表头
                        treeview.heading("油品名称", text="油品名称")

                        treeview.pack(side=tk.LEFT, fill=tk.BOTH)

                        bianhao = ['001', '002', '003', '004', '005']
                        name = ['石脑油', '汽油','柴油','煤油','原油']
                        for i in range(min(len(bianhao), len(name))):  # 写入数据
                            treeview.insert('', i, values=(bianhao[i], name[i]))

                        def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
                            l = [(tv.set(k, col), k) for k in tv.get_children('')]
                            l.sort(reverse=reverse)  # 排序方式
                            # rearrange items in sorted positions
                            for index, (val, k) in enumerate(l):  # 根据排序后索引移动
                                tv.move(k, '', index)
                            tv.heading(col,
                                       command=lambda: treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

                        def set_cell_value(event):  # 双击进入编辑状态
                            for item in treeview.selection():
                                # item = I001
                                item_text = treeview.item(item, "values")
                                # print(item_text[0:2])  # 输出所选行的值
                            column = treeview.identify_column(event.x)  # 列
                            row = treeview.identify_row(event.y)  # 行
                            cn = int(str(column).replace('#', ''))
                            rn = int(str(row).replace('I', ''))
                            entryedit = tk.Text(from8, width=10 + (cn - 1) * 16, height=1)
                            entryedit.place(x=16 + (cn - 1) * 130, y=6 + rn * 20)

                            def saveedit():
                                treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
                                entryedit.destroy()
                                okb.destroy()

                            okb = ttk.Button(from8, text='OK', width=4, command=saveedit)
                            okb.place(x=90 + (cn - 1) * 242, y=2 + rn * 20)

                        def newrow():
                            bianhao.append('请输入编号')
                            name.append('请输入浮盘名称')
                            treeview.insert('', len(bianhao) - 1,
                                            values=(bianhao[len(bianhao) - 1], name[len(bianhao) - 1]))
                            treeview.update()
                            newb.place(x=180, y=(len(bianhao) - 1) * 20 + 45)
                            newb.update()

                        treeview.bind('<Double-1>', set_cell_value)  # 双击左键进入编辑
                        newb = ttk.Button(from8, text='新增', width=10, command=newrow)
                        newb.place(x=180, y=(len(bianhao) - 1) * 20 + 45)

                        for col in columns:  # 绑定函数，使表头可排序
                            treeview.heading(col, text=col,
                                             command=lambda _col=col: treeview_sort_column(treeview, _col, False))

                        from8.mainloop()
                    def fupanclick():
                        from3 = tk.Tk()  # 初始框的声明
                        from3.title("浮盘")
                        columns = ("浮盘编号", "浮盘名称")
                        treeview = ttk.Treeview(from3, height=18, show="headings", columns=columns)  # 表格

                        treeview.column("浮盘编号", width=100, anchor='center')  # 表示列,不显示
                        treeview.column("浮盘名称", width=300, anchor='center')

                        treeview.heading("浮盘编号", text="浮盘编号")  # 显示表头
                        treeview.heading("浮盘名称", text="浮盘名称")

                        treeview.pack(side=tk.LEFT, fill=tk.BOTH)

                        bianhao = ['001', '002']
                        name = ['新浮盘', '旧浮盘']
                        for i in range(min(len(bianhao), len(name))):  # 写入数据
                            treeview.insert('', i, values=(bianhao[i], name[i]))

                        def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
                            l = [(tv.set(k, col), k) for k in tv.get_children('')]
                            l.sort(reverse=reverse)  # 排序方式
                            # rearrange items in sorted positions
                            for index, (val, k) in enumerate(l):  # 根据排序后索引移动
                                tv.move(k, '', index)
                            tv.heading(col,
                                       command=lambda: treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

                        def set_cell_value(event):  # 双击进入编辑状态
                            for item in treeview.selection():
                                # item = I001
                                item_text = treeview.item(item, "values")
                                # print(item_text[0:2])  # 输出所选行的值
                            column = treeview.identify_column(event.x)  # 列
                            row = treeview.identify_row(event.y)  # 行
                            cn = int(str(column).replace('#', ''))
                            rn = int(str(row).replace('I', ''))
                            entryedit = tk.Text(from3, width=10 + (cn - 1) * 16, height=1)
                            entryedit.place(x=16 + (cn - 1) * 130, y=6 + rn * 20)

                            def saveedit():
                                treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
                                entryedit.destroy()
                                okb.destroy()

                            okb = ttk.Button(from3, text='OK', width=4, command=saveedit)
                            okb.place(x=90 + (cn - 1) * 242, y=2 + rn * 20)

                        def newrow():
                            bianhao.append('请输入编号')
                            name.append('请输入浮盘名称')
                            treeview.insert('', len(bianhao) - 1,
                                            values=(bianhao[len(bianhao) - 1], name[len(bianhao) - 1]))
                            treeview.update()
                            newb.place(x=180, y=(len(bianhao) - 1) * 20 + 45)
                            newb.update()

                        treeview.bind('<Double-1>', set_cell_value)  # 双击左键进入编辑
                        newb = ttk.Button(from3, text='新增', width=10, command=newrow)
                        newb.place(x=180, y=(len(bianhao) - 1) * 20 + 45)

                        for col in columns:  # 绑定函数，使表头可排序
                            treeview.heading(col, text=col,
                                             command=lambda _col=col: treeview_sort_column(treeview, _col, False))

                        from3.mainloop()
                        pass

                    def mifengclick():
                        from4 = tk.Tk()  # 初始框的声明
                        from4.title("密封形式")
                        columns = ("密封编号", "密封形式")
                        treeview = ttk.Treeview(from4, height=18, show="headings", columns=columns)  # 表格

                        treeview.column("密封编号", width=100, anchor='center')  # 表示列,不显示
                        treeview.column("密封形式", width=300, anchor='center')

                        treeview.heading("密封编号", text="密封编号")  # 显示表头
                        treeview.heading("密封形式", text="密封形式")

                        treeview.pack(side=tk.LEFT, fill=tk.BOTH)

                        mifeng = ['001', '002', '003']
                        mifengtyp = ['机械密封', '液托型弹性充填式密封', '气托型弹性充填式密封']
                        for i in range(min(len(mifeng), len(mifengtyp))):  # 写入数据
                            treeview.insert('', i, values=(mifeng[i], mifengtyp[i]))

                        def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
                            l = [(tv.set(k, col), k) for k in tv.get_children('')]
                            l.sort(reverse=reverse)  # 排序方式
                            # rearrange items in sorted positions
                            for index, (val, k) in enumerate(l):  # 根据排序后索引移动
                                tv.move(k, '', index)
                            tv.heading(col,
                                       command=lambda: treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

                        def set_cell_value(event):  # 双击进入编辑状态
                            for item in treeview.selection():
                                # item = I001
                                item_text = treeview.item(item, "values")
                                # print(item_text[0:2])  # 输出所选行的值
                            column = treeview.identify_column(event.x)  # 列
                            row = treeview.identify_row(event.y)  # 行
                            cn = int(str(column).replace('#', ''))
                            rn = int(str(row).replace('I', ''))
                            entryedit = tk.Text(from4, width=10 + (cn - 1) * 16, height=1)
                            entryedit.place(x=16 + (cn - 1) * 130, y=6 + rn * 20)

                            def saveedit():
                                treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
                                entryedit.destroy()
                                okb.destroy()

                            okb = ttk.Button(from4, text='OK', width=4, command=saveedit)
                            okb.place(x=90 + (cn - 1) * 242, y=2 + rn * 20)

                        def newrow():
                            mifeng.append('请输入密封编号')
                            mifengtyp.append('请输入密封形式')
                            treeview.insert('', len(mifeng) - 1,
                                            values=(mifeng[len(mifeng) - 1], mifengtyp[len(mifeng) - 1]))
                            treeview.update()
                            newb.place(x=180, y=(len(mifeng) - 1) * 20 + 45)
                            newb.update()

                        treeview.bind('<Double-1>', set_cell_value)  # 双击左键进入编辑
                        newb = ttk.Button(from4, text='新增', width=10, command=newrow)
                        newb.place(x=180, y=(len(mifeng) - 1) * 20 + 45)

                        for col in columns:  # 绑定函数，使表头可排序
                            treeview.heading(col, text=col,
                                             command=lambda _col=col: treeview_sort_column(treeview, _col, False))

                        from4.mainloop()
                        pass

                    def mifengjiegouclick():
                        from5 = tk.Tk()  # 初始框的声明
                        from5.title("边圈密封结构")
                        columns = ("密封编号", "密封结构")
                        treeview = ttk.Treeview(from5, height=18, show="headings", columns=columns)  # 表格

                        treeview.column("密封编号", width=100, anchor='center')  # 表示列,不显示
                        treeview.column("密封结构", width=300, anchor='center')

                        treeview.heading("密封编号", text="密封编号")  # 显示表头
                        treeview.heading("密封结构", text="密封结构")

                        treeview.pack(side=tk.LEFT, fill=tk.BOTH)

                        mifeng = ['001', '002', '003', '004']
                        mifengtyp = ['只有一次密封', '有挡雨板', '密封板处有二次密封', '边圈有二次密封']
                        for i in range(min(len(mifeng), len(mifengtyp))):  # 写入数据
                            treeview.insert('', i, values=(mifeng[i], mifengtyp[i]))

                        def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
                            l = [(tv.set(k, col), k) for k in tv.get_children('')]
                            l.sort(reverse=reverse)  # 排序方式
                            # rearrange items in sorted positions
                            for index, (val, k) in enumerate(l):  # 根据排序后索引移动
                                tv.move(k, '', index)
                            tv.heading(col,
                                       command=lambda: treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

                        def set_cell_value(event):  # 双击进入编辑状态
                            for item in treeview.selection():
                                # item = I001
                                item_text = treeview.item(item, "values")
                                # print(item_text[0:2])  # 输出所选行的值
                            column = treeview.identify_column(event.x)  # 列
                            row = treeview.identify_row(event.y)  # 行
                            cn = int(str(column).replace('#', ''))
                            rn = int(str(row).replace('I', ''))
                            entryedit = tk.Text(from5, width=10 + (cn - 1) * 16, height=1)
                            entryedit.place(x=16 + (cn - 1) * 130, y=6 + rn * 20)

                            def saveedit():
                                treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
                                entryedit.destroy()
                                okb.destroy()

                            okb = ttk.Button(from5, text='OK', width=4, command=saveedit)
                            okb.place(x=90 + (cn - 1) * 242, y=2 + rn * 20)

                        def newrow():
                            mifeng.append('请输入密封编号')
                            mifengtyp.append('请输入密封结构')
                            treeview.insert('', len(mifeng) - 1,
                                            values=(mifeng[len(mifeng) - 1], mifengtyp[len(mifeng) - 1]))
                            treeview.update()
                            newb.place(x=180, y=(len(mifeng) - 1) * 20 + 45)
                            newb.update()

                        treeview.bind('<Double-1>', set_cell_value)  # 双击左键进入编辑
                        newb = ttk.Button(from5, text='新增', width=10, command=newrow)
                        newb.place(x=180, y=(len(mifeng) - 1) * 20 + 45)

                        for col in columns:  # 绑定函数，使表头可排序
                            treeview.heading(col, text=col,
                                             command=lambda _col=col: treeview_sort_column(treeview, _col, False))

                        from5.mainloop()
                        pass

                    def jisuanclick():
                        jisunafrom = tk.Tk()
                        jisunafrom.title("计算器")

                        jisunafrom.geometry("292x321")

                        # 定义函数
                        def jisuan(e):
                            # print(e.configure().get("text")[-1])
                            v = str((e.widget.configure().get("text")[-1]))
                            if "=" in var1.get():
                                var1.set("")
                            if v == "清空":
                                var1.set("")
                            elif v == "退格":
                                var1.set(var1.get()[0:len(var1.get()) - 1])  # 得到列表内所有不包括最后一位
                            # elif v=="x":
                            #     var1.set(var1.get() +"*")
                            else:
                                var1.set(var1.get() + v)
                            # print(e.widget.configure())
                            pass

                        def bdengclick():
                            try:
                                result = eval(var1.get())
                                var1.set(var1.get() + "=" + str(result))
                            except:
                                mesbox.showwarning("erro", "请输入正确的计算公式")
                            pass

                        # 第一部分
                        # 声明变量绑定enyry控件
                        var1 = tk.StringVar()
                        entry1 = tk.Entry(jisunafrom, background="#184048", textvariable=var1, fg="white")
                        entry1.grid(row=0, column=0, sticky=tk.EW, ipady=20)
                        # 第二部分
                        # 创建frame框架
                        f1 = tk.Frame(jisunafrom)
                        f1.grid(row=1, column=0)
                        # 创建按钮与按钮文本的列表
                        fh = [7, 8, 9, "*", "4", "5", "6", "-", "1", "2", "3", "+", "0", ".", "清空", "退格"]
                        # 行列的变量
                        ri = 0
                        ci = 0
                        # 通过循环生出所有的按钮
                        labelsize = font.Font(size=10, family="楷体")
                        for v in fh:
                            if ci != 0 and ci % 4 == 0:
                                ri += 1  # 换行
                                ci = 0  # 列重新赋值
                            # b1=tk.Button(f1,text=v,width=8,command=lambda:jisuan(b1))
                            b1 = tk.Button(f1, text=v, width=8, font=labelsize, fg="white", bg="#48504d")
                            b1.bind("<Button-1>", jisuan)
                            b1.grid(row=ri, column=ci, ipady=15)
                            ci += 1
                        bdeng = tk.Button(f1, text="=", command=bdengclick, font=labelsize, bg="#48504d")
                        bdeng.grid(row=ri + 1, column=0, columnspan=4, sticky=tk.EW)
                        jisunafrom.mainloop()
                        pass

                    def quictclick():
                        top.destroy()
                        pass

                    def guanyuclick():
                        from7 = tk.Tk()
                        from7.title("关于")
                        from7.geometry("230x300")
                        from7lab1=tk.Label(from7,text="版本号：6.0.1")
                        from7lab1.place(x=30,y=5)
                        from7lab2 = tk.Label(from7, text="版权所有：常州大学")
                        from7lab2.place(x=30, y=220)
                        from7lab3 = tk.Label(from7, text="石油工程学院")
                        from7lab3.place(x=80, y=240)
                        from7text = tk.Text(from7, width=25, height=14, background="#f5f5f5")
                        from7text.place(x=30, y=30)
                        # from7pic2 = Image.open("./img/logo1.png")
                        # # 定义照片大小
                        # w, h = from7pic2.size
                        # from7pic2 = from7pic2.resize((int(0.2 * w), int(0.2 * h)))
                        # from7pho2 = ImageTk.PhotoImage(from7pic2)
                        # from7text.image_create(tk.END, image=from7pho2)
                        from7text.tag_config("f1", font=("宋体", 10), foreground="black")
                        from7text.insert(tk.END, """软件设计：常州大学
     石油工程学院
 如果您一旦安装、复制或以其
他方式使用本软件，请注意：
本软件是在常州大学石油工程
学院软件研发组开发完成的。
未经软件开发者授权许可不得
擅自发布该软件。

警告: 本计算机程序受著作权
法和国际公约的保护，未经授
权擅自复制或散布本程序的部
分或全部，将承受严厉的民事
和刑事处罚，对已知的违反者
将给予法律范围内的全面制裁
。
如果您对本软件有任何疑问，
或因任何原因希望联络我们，
请给我们来信。

""", "f1")

                        pass

                    # 配置窗体菜单模块
                    menubar = tk.Menu(self.master)
                    self.master.s1=tk.PhotoImage(file="盘1.png")
                    self.master.s2 = tk.PhotoImage(file="密封1.png")
                    self.master.s3= tk.PhotoImage(file="结构1.png")
                    self.master.s4 = tk.PhotoImage(file="浓度1.png")
                    self.master.s5 = tk.PhotoImage(file="退出1.png")
                    self.master.s6 = tk.PhotoImage(file="喷涂1.png")
                    self.master.s7 = tk.PhotoImage(file="罐1.png")
                    self.master.s8 = tk.PhotoImage(file="静1.png")
                    self.master.s9 = tk.PhotoImage(file="计算器1.png")
                    self.master.s10 = tk.PhotoImage(file="关于1.png")
                    self.master.s11 = tk.PhotoImage(file="系数1.png")
                    self.master.s30 = tk.PhotoImage(file="油1.png")


                    # 大菜单
                    menu1 = tk.Menu(menubar, tearoff=False)
                    menu1.add_command(label="浮盘", command=fupanclick,image=self.master.s1,compound="left")
                    menu1.add_command(label="油品种类",command=youpinclick,image=self.master.s30,compound="left")
                    menu1.add_command(label="密封形式", command=mifengclick, image=self.master.s2,compound="left")
                    menu1.add_command(label="边圈密封结构", command=mifengjiegouclick, image=self.master.s3,compound="left")
                    menu1.add_command(label="油品气体浓度范围", command=zhongleiclick, image=self.master.s4,compound="left")
                    # 创建分隔符
                    menu1.add_separator()
                    menu1.add_command(label="退出", command=quictclick,image=self.master.s5,compound="left")

                    menubar.add_cascade(label="基础数据", menu=menu1)
                    menu3=tk.Menu(menubar,tearoff=False)
                    menu3.add_command(label="外浮顶罐损耗",image=self.master.s7,compound="left")
                    menu3.add_command(label="静储损耗",image=self.master.s8,compound="left")
                    menu3.add_command(label="输储(内壁无喷涂内衬)损耗",image=self.master.s6,compound="left")
                    menubar.add_cascade(label="蒸发损耗",menu=menu3)
                    menu4=tk.Menu(menubar,tearoff=False)
                    menu4.add_command(label="损耗系数",image=self.master.s11,compound="left")
                    menubar.add_cascade(label="损耗系数",menu=menu4)

                    menu2 = tk.Menu(menubar, tearoff=False)
                    menu2.add_command(label='计算器', command=jisuanclick,image=self.master.s9,compound="left")
                    menu2.add_command(label='关于', command=guanyuclick,image=self.master.s10,compound="left")
                    menubar.add_cascade(label="帮助", menu=menu2)
                    self.master.config(menu=menubar)


                    def gettime():
                        # 获取当前时间并转为字符串
                        timestr = time.strftime("%Y/%m/%d %H:%M:%S")
                        # 重新设置标签文本
                        labtime.configure(text=timestr)
                        # 每隔一秒调用函数gettime自身获取时间
                        self.master.after(1000, gettime)

                    labtime = tk.Label(self.master, text="", fg="black", font=("宋体", 14))
                    labtime.place(x=300, y=605)
                    labfont = tk.Label(self.master, text="欢迎使用本软件,现在时间是：", fg="black", font=("楷体", 14))
                    labfont.place(x=25, y=605)
                    labfont3 = tk.Label(self.master, text="祝您生活愉快！", fg="black", font=("楷体", 15))
                    labfont3.place(x=500, y=605)
                    labfont2 = tk.Label(self.master, text="BY: Huang wei qiu", fg="black", font=("宋体", 14))
                    labfont2.place(x=710, y=605)
                    gettime()
                    picT = Image.open("./img/z.jpg")
                    phoT = ImageTk.PhotoImage(picT)
                    labT=ttk.Label(fram0text1,text="nihao",Image=phoT)
                    labT.place(x=0,y=10)




            class Application(Application_ui):
                # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
                def __init__(self, master=None):
                    Application_ui.__init__(self, master)


            if __name__ == "__main__":
                top = tk.Tk()
                top.resizable(width=False, height=True)
                Application(top).mainloop()
        else:
            mesbox.showerror(message='Error, your password is wrong, try again.')
    else:  # 如果发现用户名不存在
        is_sign_up = mesbox.askyesno('Welcome！ ', 'You have not sign up yet. Sign up now?')
        # 提示需不需要注册新用户
        if is_sign_up:
            btn2click()
    #开始主程序窗口

def btn2click():
    def btn3click():
        np=entry4.get()
        nn=entry3.get()
        npc=entry5.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
            if np != npc:
                mesbox.showerror('Error', 'Password and confirm password must be the same!')

                # 如果用户名已经在我们的数据文件中，则提示Error, The user has already signed up!
            elif nn in exist_usr_info:
                mesbox.showerror('Error', 'The user has already signed up!')
            else:
                exist_usr_info[nn] = np
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                mesbox.showinfo('欢迎', '您已注册成功!')
                # 然后销毁窗口。
                from2.destroy()


    #窗口上的窗口
    from2=tk.Toplevel(from1);from2.title("注册新用户")
    w=300;h=200
    sw=from1.winfo_screenwidth();sh=from1.winfo_screenheight()
    x=sw/2-w/2;y=sh/2-h/2-50
    from2.geometry("%dx%d+%d+%d"%(w,h,x,y))
    # 注册界面的按钮和标签
    lab3 = tk.Label(from2, text="用户名:")
    lab3.place(x=82, y=10)
    varnewname = tk.StringVar
    entry3 = tk.Entry(from2, textvariable=varnewname)
    entry3.place(x=130, y=10)
    lab4 = tk.Label(from2, text="密码:")
    lab4.place(x=92, y=50)
    varnewpassword = tk.StringVar
    entry4 = tk.Entry(from2, textvariable=varnewpassword, show="*")
    entry4.place(x=130, y=50)
    lab5 = tk.Label(from2,text="确认您的密码：")
    lab5.place(x=45, y=90)
    varpasswordconfirm = tk.StringVar()
    entry5 = tk.Entry(from2, textvariable=varpasswordconfirm, show="*")
    entry5.place(x=130, y=90)
    btn3 = tk.Button(from2, text="注册", command=btn3click,image=from1.s13,compound="left")
    btn3.place(x=150, y=130)
    from2.resizable(width=False, height=True)



#窗口图片
pic1=Image.open("./img/1.png")
pho1=ImageTk.PhotoImage(pic1)
lab1=tk.Label(from1,image=pho1)
lab1.pack(side="top")

ztext=tk.Text(from1,width=18,height=11,background="#f5f5f5")
ztext.place(x=50,y=320)
pic2=Image.open("./img/logo.png")
#定义照片大小
w,h=pic2.size
pic2=pic2.resize((int(0.2*w),int(0.2*h)))
pho2=ImageTk.PhotoImage(pic2)
ztext.image_create(tk.END,image=pho2)
ztext.tag_config("f1",font=("楷体",13),foreground="black")
ztext.insert(tk.END,"   "+" 常州大学 "+"\n"+" "+
                    "石油工程学院","f1")

from1.s12 = tk.PhotoImage(file="用户1.png")
from1.s13 = tk.PhotoImage(file="注册1.png")

#窗口下文字
labx=tk.Label(from1, text='油品损耗计算及信息存储系统v6.0.1',font=('Arial', 15),fg="#363636")
labx.place(x=150,y=280)
#标签,输入框
lab1=tk.Label(from1,text="用户名:",font=("宋体",12))
lab1.place(x=190,y=355)
varusername=tk.StringVar()
entry1=tk.Entry(from1,font=("Arial",12),textvariable=varusername)
entry1.place(x=260,y=355,height=25)
varusername.set("admin")
lab2=tk.Label(from1,text="密码:",font=("宋体",12))
lab2.place(x=205,y=405)
varpassword=tk.StringVar()
entry2=tk.Entry(from1,font=("Arial",12),show="*",textvariable=varpassword)
entry2.place(x=260,y=405,height=25)
varpassword.set("admin")
#创建按钮
# btntimage=tk.PhotoImage(file='登录1.png')
# btnt=tk.Button(from1,text="登录",image=btntimage,font=("黑体",12))
# btnt.place(x=268,y=450,width=40)
btn1=tk.Button(from1,text="登录",font=("黑体",12),command=btn1click,image=from1.s12,compound="left")
btn1.place(x=268,y=450,width=80)

# btnt.configure(image=btntimage)

btn2=tk.Button(from1,text="注册",font=("黑体",12),command=btn2click,image=from1.s13,compound="left")
btn2.place(x=360,y=450,width=80)
from1.resizable(width=False, height=True)
from1.mainloop()