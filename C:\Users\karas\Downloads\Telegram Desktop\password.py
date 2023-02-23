from  tkinter import *
from random import *
def onClick():
    r = ''
    dl = int(e.get())
    for i in range(dl) :
        r = r + c[randint(0,130)]
    resultLabel.config(text=r)

c =tuple('qwertyuiopasdfghjkl;zxcvbnm,QWERTYUIOPASDFGHJKL:ZXCVBNM1234567890-=_+йцукенгшщзфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')
root=Tk()
root.title('aaa')
root.geometry('500x300')

Label(text ='длина пароля').pack()
e = Entry(text ='длина пароля')
e.pack()

resultLabel = Label(root)
resultLabel.pack()
