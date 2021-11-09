# -*- coding: UTF-8 -*-
import socket
import threading
import tkinter
import random
from tkinter import ttk
import ttkthemes

# 服务器/服务端IP地址
ip = ''


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 1234))
Port = (ip, 1234)
# Port = ('127.0.0.1', 1234)
name_list = [
    '唐僧', '孙悟空', '猪八戒', '沙悟净', '白龙马', '如来佛',
    '燃灯古佛', '弥勒佛', '观音', '文殊菩萨', '普贤菩萨', '地藏菩萨',
    '大迦叶', '阿难', '灵吉菩萨', '毗蓝婆菩萨', '骑鹿罗汉', '喜庆罗汉',
    '举钵罗汉', '托塔罗汉', '挣坐罗汉', '过江罗汉', '骑象罗汉', '笑狮罗汉',
    '开心罗汉', '探手罗汉', '沉思罗汉', '挖耳罗汉', '布袋罗汉', '芭蕉罗汉',
    '长眉罗汉', '看门罗汉', '降龙罗汉', '伏虎罗汉', '东方持国天王', '南方增长天王',
    '西方广目天王', '北方多闻天王', '太上老君', '玉皇大帝', '西王母', '骊山老母',
    '太乙救苦天尊', '太白金星', '福星', '禄星', '南极寿星', '紫阳真人',
    '托塔天王李靖', '哪吒', '巨灵神', '二郎神杨戬', '昴日星官', '赤脚大仙',
    '镇元大仙', '如意真仙', '菩提祖师', '太阴星君', '东海龙王', '西海龙王',
    '南海龙王', '北海龙王', '火德星君', '水德星君', '雷公', '闪电娘娘',
    '风伯', '雨师', '门神秦琼', '门神尉迟恭', '金顸大仙', '土地公',
    '六耳猕猴', '灵感大王', '青牛精', '黄袍怪', '黄风怪', '蝎子精',
    '金角大王', '银角大王', '黑熊精', '铁扇公主', '牛魔王', '九头怪',
    '玉面公主', '黄眉大王', '蟒蛇精', '百眼魔君', '蜘蛛精', '赛太岁',
    '鼍龙', '玉兔精', '红孩儿', '虎力大仙', '鹿力大仙', '羊力大仙',
    '狮猁怪', '青毛狮子怪', '黄牙老象', '金翅大鹏雕', '白鹿精', '白骨精',
    '金鼻白毛老鼠精', '艾叶花皮豹子精', '九灵元圣', '黄狮精', '通天河老鼋', '唐太宗',
    '魏征', '渔翁张稍', '樵子李定', '东方朔', '宝象国国王', '朱紫国国王',
    '乌鸡国国王', '西梁女国国王',
    '及时雨', '玉麒麟', '智多星', '入云龙', '大刀', '豹子头',
    '霹雳火', '双鞭', '小李广', '小旋风', '扑天雕', '美髯公',
    '花和尚', '行者', '双枪将', '没羽箭', '青面兽', '金枪手',
    '急先锋', '神行太保', '赤发鬼', '黑旋风', '九纹龙', '没遮拦',
    '插翅虎', '混江龙', '立地太岁', '船火儿', '短命二郎', '浪里白条',
    '活阎罗', '病关索', '拼命三郎', '两头蛇', '双尾蝎', '浪子',
    '神机军师', '镇三山', '病尉迟', '丑郡马', '井木犴', '百胜将',
    '天目将', '圣水将', '神火将', '圣手书生', '铁面孔目', '摩云金翅',
    '火眼狻猊', '锦毛虎', '锦豹子', '轰天雷', '神算子', '小温侯',
    '赛仁贵', '神医', '紫髯伯', '矮脚虎', '一丈青', '丧门神',
    '混世魔王', '毛头星', '独火星', '八臂哪吒', '飞天大圣', '玉臂匠',
    '铁笛仙', '出洞蛟', '翻江蜃', '玉幡竿', '通臂猿', '跳涧虎',
    '白花蛇', '白面郎君', '九尾龟', '铁扇子', '铁叫子', '花项虎',
    '中箭虎', '小遮拦', '操刀鬼', '云里金刚', '摸着天', '病大虫',
    '金眼彪', '打虎将', '小霸王', '金钱豹子', '鬼脸儿', '出林龙',
    '独角龙', '旱地忽律', '笑面虎', '铁臂膊', '一枝花', '催命判官',
    '青眼虎', '没面目', '石将军', '小尉迟', '母大虫', '菜园子',
    '母夜叉', '活闪婆', '险道神郁保四', '白日鼠', '鼓上蚤', '金毛犬',
]

name = random.sample(name_list, 1)[0]
s.sendto(bytes('[%s] 进入房间' % name, encoding='utf-8'), Port)


def send():
    if not text_input.get(1.0, 1.1):
        return
    text = text_input.get(1.0, 'end')

    while len(text) and text[-1] == '\n':
        text = text.rstrip()

    data = name + ': ' + text
    s.sendto(bytes(data, encoding='utf-8'), Port)

    text_input.delete(1.0, 'end')


def receive():
    while True:
        data = s.recvfrom(102400)
        data = str(data[0], encoding='utf-8')

        if data == 'stop':
            break

        if data[0] == '>':
            label_number.configure(text='在线人数: ' + data[1:])
            continue

        if data[0] != '<' or text_show.get(1.0, 1.1):
            data = '\n\n' + data

        text_show.config(state='normal')
        text_show.insert('end', data)
        text_show.see('end')
        text_show.config(state='disable')


def rename():
    global name
    name = random.sample(name_list, 1)[0]
    label_name.configure(text='当前名称: %s' % name)

    data = '>' + name
    s.sendto(bytes(data, encoding='utf-8'), Port)


window = tkinter.Tk()
window.title('匿名聊天室')
window.geometry('500x700')

text_show = tkinter.Text()
text_show.configure(font=("", 16))  # fg='blue
text_show.config(state='disable')

text_input = tkinter.Text()
text_input.configure(font=("", 12))

scroll = ttk.Scrollbar()
scroll.config(command=text_show.yview)
text_show.config(yscrollcommand=scroll.set)


button_send = ttk.Button(text='发送', command=send)
label_number = ttk.Label(text='在线人数: 0', font=('', 14), anchor='w')
label_name = tkinter.Label(text='当前名称: %s' % name, font=('', 14), anchor='w')
button_name = ttk.Button(text='更改', command=rename)

style = ttkthemes.ThemedStyle(window)
style.set_theme('breeze')

label_name.place(x=170, y=20, width=210, height=30)
label_number.place(x=20, y=20, width=150, height=30)
button_name.place(x=390, y=20, width=50, height=30)
text_show.place(x=20, y=70, width=440, height=500)
scroll.place(x=460, y=70, width=20, height=500)
text_input.place(x=20, y=590, width=370, height=60)
button_send.place(x=410, y=590, width=70, height=60)

thread_receive = threading.Thread(target=receive, name='receive')
thread_receive.start()


def close_():
    window.destroy()
    s.sendto(bytes("exit", encoding='utf-8'), Port)


window.protocol("WM_DELETE_WINDOW", close_)
window.mainloop()
