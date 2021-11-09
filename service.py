import socket
import time
import threading
import tkinter

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 1234))
addr_list = set()
port_list = {}
name_list = {}
length = 0


def data_receive():
    global length
    while True:
        data = s.recvfrom(102400)

        # 进入房间
        if str(data[0], encoding='utf-8')[0] == '[':
            addr_list.add(data[1][0])
            port_list[data[1][0]] = data[1]
            name_list[data[1][0]] = str(data[0], encoding='utf-8').split(']')[0][1:]

            online_num()
            for addr in addr_list:
                message = '<系统> ' + str(data[0], encoding='utf-8')
                s.sendto(bytes(message, encoding='utf-8'), port_list[addr])

        # 改名请求
        elif str(data[0], encoding='utf-8')[0] == '>':
            name_list[data[1][0]] = str(data[0], encoding='utf-8')[1:]

            text.delete(0, 'end')
            for addr in addr_list:
                text.insert('end', name_list[addr])

        # 离开房间
        elif str(data[0], encoding='utf-8') == "exit":
            addr_list.discard(data[1][0])
            s.sendto(bytes('stop', encoding='utf-8'), port_list[data[1][0]])

        # 正常对话
        else:
            for addr in addr_list:
                message = time.strftime('%H:%M:%S\n') + str(data[0], encoding='utf-8')
                s.sendto(bytes(message, encoding='utf-8'), port_list[addr])

        # 在线人数
        if len(addr_list) != length:
            length = len(addr_list)
            online_num()


def online_num():
    label.configure(text='在线人数: %d' % length)

    text.delete(0, 'end')
    for addr in addr_list:
        temp = '>%d' % length
        s.sendto(bytes(temp, encoding='utf-8'), port_list[addr])
        text.insert('end', name_list[addr])


def close_():
    for addr in addr_list:
        s.sendto(bytes('stop', encoding='utf-8'), port_list[addr])
    window.destroy()


thread_receive = threading.Thread(target=data_receive, name='receive')
thread_receive.start()

window = tkinter.Tk()
window.geometry('500x700')

label = tkinter.Label(text='在线人数: %d' % length, font=('', 14), anchor='w')
text = tkinter.Listbox()
text.configure(font=("", 16))

label.place(x=20, y=20, width=150, height=30)
text.place(x=20, y=70, width=460, height=500)

window.protocol("WM_DELETE_WINDOW", close_)
window.mainloop()
