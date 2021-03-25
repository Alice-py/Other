"""
开发时间：2019-4-20
作者：Honeypot
邮箱：1104389956@qq.com
版本：1.5
1.2改动：添加了快捷键（翻译：Enter  清空：Esc）
            修复信息框可键入内容，修复初始光标指向
1.3改动：窗口置顶，添加了快捷键（退出：Ctrl+q )
1.5改动：单行文本框改为多行文本框，修改窗口样式，修复部分bug     2019-5-19
"""

from urllib import request, parse
import json
import tkinter as tk
import sys


def formatting(_strs):
    # 接受str，返回json
    json_dict = dict()
    _str_list = _strs.split("\n")
    for _str in _str_list:
        if ":" not in _str:
            _str_list.remove(_str)
            continue
        _list = _str.split(":")
        json_dict[_list[0].strip()] = _list[1].strip()
    json_dict = json.dumps(json_dict)
    return json_dict


def gui():
    # 主窗口属性模块
    win.resizable(width=False, height=False)  # 禁止拉伸
    win['background'] = '#F0FFF0'  # 设置背景颜色
    win.title('Json转换')  # 标题
    win.geometry('400x420-50+50')  # 窗口大小与其实坐标


def get_str(meaningless=None):
    # 事件1-获取文本

    var2.config(state='normal')
    var2.delete(1.0, 'end')

    vart = var1.get("0.0", "end")

    return_txt = formatting(vart)
    var2.insert('end', return_txt)
    var2.config(state='disabled')


def clean_var(meaningless=None):
    var2.config(state='normal')
    var1.delete(1.0, 'end')
    var2.delete(1.0, 'end')
    var2.config(state='disabled')


def over(meaningless=None):
    sys.exit()


if __name__ == '__main__':
    win = tk.Tk()
    win.wm_attributes('-topmost', 1)  # 置顶
    gui()

    # 文本框1
    # var1 = tk.Entry(win, width=200, font=('Fixdsys', 16))

    var1 = tk.Text(win, height=10, font=('Fixdsys', 12))
    var1.pack(pady=0)  # 样式

    # 确认按钮
    var1.bind("<Return>", get_str)  # 绑定回车
    target_content = tk.Button(
        win,
        text='OK',
        command=get_str,
        width=30,
        height=2,
        bg='#F0FFF0',
        bd=0).place(
        x=0,
        y=145)
    var1.focus()

    # 清除按钮
    var1.bind("<Escape>", clean_var)  # 绑定回车
    tk.Button(
        win,
        text='Clean',
        command=clean_var,
        width=30,
        height=2,
        bg='#F0FFF0',
        bd=0).place(
        x=200,
        y=145)

    # 文本框2
    var2 = tk.Text(win, height=12, font=('Fixdsys', 14))
    var2.pack(side='bottom')  # 样式
    var2.config(state='disabled')
    win.bind('<Control-q>', over)
    win.mainloop()

#
# import json
# import tkinter as tk
# from tkinter import *
# import sys
#
# class VITUJSON:
#     def __init__(self):
#         self.win = tk.Tk()
#
#     def gui(self):
#         # 主窗口属性模块， 相当于初始化设置
#         self.win.wm_attributes('-topmost', 1)
#         self.win.resizable(width=False, height=False)  # 禁止拉伸
#         self.win['background'] = '#F0FFF0'  # 设置背景颜色
#         self.win.title('Headers Turn JSON')  # 标题
#         self.win.geometry('500x450-50+50')  # 窗口大小与其实坐标
#
#
#     def gui_generate_text(self):
#         # # 生成文本框
#         self.var1 = tk.Text(self.win, height=10, font=('Fixdsys', 12))
#         self.var1.pack(pady=0)  # 样式
#
#         self.var2 = tk.Text(self.win, height=12, font=('Fixdsys', 14))
#         self.var2.pack(side='bottom')  # 样式
#         self.var2.config(state='disabled')
#         return self.var1, self.var2
#
#     def lable1(self):
#         # 获取文本框的内容，由于事件触发会直接执行此函数并不再继续后面动作，固写与此
#         vart = self.var1.get("0.0", "end")
#         target_json = self.formatting(vart)
#         print(target_json)
#         return vart
#
#     def gui_bind_event(self):
#         # # 绑定按钮
#         # self.var1.get("0.0", "end")
#         tk.Button(
#             self.win,
#             text='转换',
#             command=self.lable1,    # 将事件绑定在此，注意不要带括号
#             width=30,
#             height=2,
#             bg='#F0FFF0',
#             bd=0).place(
#             x=140,
#             y=170)
#         self.var1.focus()
#
#
#
#     def formatting(self, _str):
#         # 接受str，返回json
#         json_dict = dict()
#         _str_list = _strs.split("\n")
#         for _str in _str_list:
#             if ":" not in _str:
#                 _str_list.remove(_str)
#                 continue
#             _list = _str.split(":")
#             json_dict[_list[0].strip()] = _list[1].strip()
#         return json_dict
#
#
#
#     def main(self):
#         # json_str = self.formatting(_str)
#         # print(json_str)
#         self.gui()
#         self.gui_generate_text()
#         self.gui_bind_event()
#
#
#
#         self.win.mainloop()
#
#
#
#
# if __name__ == '__main__':
#     _strs = """
#     POST /index.php/login HTTP/1.1
#     Host: wp.honeypot.work
#     Connection: keep-alive
#     Content-Length: 189
#     Cache-Control: max-age=0
#     Upgrade-Insecure-Requests: 1
#     Origin: null
#     Content-Type: application/x-www-form-urlencoded
#     User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
#     Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
#     Accept-Encoding: gzip, deflate
#     Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
#     Cookie: nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true; oc_sessionPassphrase=3mdFgZUFsNKdRjfwCoSwU7Y2SMQ5HkAtF3O3eP8cR%2FQmzZEfnnWAJv468fBBgspMVGLI5kVS0%2FZVjoo8LuQn4OnUgeAq7hNJroFZfIv2R%2FBvjM51AP7%2Fwipa66gkOj2n; ocovrgosksgm=i3g4biru01gck6lr1cacp5661t
#     """
#     vi = VITUJSON().main()


# from tkinter import *
# root = Tk()  # 创建窗口对象的背景色
# # 创建两个列表
# # li = ['C', 'python', 'php', 'html', 'SQL', 'java']
# # movie = ['CSS', 'jQuery', 'Bootstrap']
# listb = Listbox(root)  # 创建两个列表组件
# listb2 = Listbox(root)
# # for item in li:  # 第一个小部件插入数据
# #     listb.insert(0, item)
# #
# # for item in movie:  # 第二个小部件插入数据
# #     listb2.insert(0, item)
#
# listb.pack()  # 将小部件放置到主窗口中
# listb2.pack()
# root.mainloop()  # 进入消息循环
