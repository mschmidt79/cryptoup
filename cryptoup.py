#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import * # Вызываем модуль tkinter
from tkinter.filedialog import * # Вызываем модуль filedialog для выбора файлов
from tkinter.messagebox import * # Вызываем модуль messagebox для вывода сообщений
 
def open_vol():
    op = askopenfilename() #Присваиваем переменной op путь и имя открываемого файла
    e1.insert(END,op) #Вставляем переменную op в текстовое поле
  
def about():
        showinfo("svedbox", "This software as a whole. Copyright © 2014 svedbox@gmail.com. All rights reserved.")

def close_win():
     root.destroy() #Закрываем программу (окно)



root = Tk() #Запуск окна программы

root.title("Cryptoup") #Заголовок программы
root.geometry('700x100+300+200')
root.resizable(False, False) # размер окна может быть изменен только по горизонтали

l1 = Label(root, text="Volume: ")
l1.pack( side = LEFT)

e1 = Entry(root,width=40)
e1.pack(side=LEFT)

btn1 = Button(root, text="Select file", width=5, bg="white",fg="black", command = open_vol) 
btn1.pack(side = LEFT)

btn2 = Button(root, text="Mount", width=5, bg="white",fg="black", command = about) 
btn2.pack(side = LEFT)

m = Menu(root) 
root.config(menu=m) 
 
fm = Menu(m) 
m.add_cascade(label="Volume",menu=fm) 
fm.add_command(label="Select file",command=open_vol) 
fm.add_command(label="Mount volume",command=open_vol)
fm.add_command(label="Dismount volume",command=about)
fm.add_command(label="Exit",command=close_win)

pm = Menu(m) 
m.add_cascade(label="Help",menu=pm) 
pm.add_command(label="About",command=about) 



root.mainloop() 

