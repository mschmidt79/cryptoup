#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import * # Вызываем модуль tkinter
from tkinter.filedialog import * # Вызываем модуль filedialog для выбора файлов
from tkinter.messagebox import * # Вызываем модуль messagebox для вывода сообщений
 
def open_vol():
    op = askopenfilename() #Присваиваем переменной op путь и имя открываемого файла
    txt.insert(END,op) #Вставляем переменную op в текстовое поле
  
def about():
        showinfo("svedbox", "This software as a whole. Copyright © 2014 svedbox@gmail.com. All rights reserved.")

def close_win():
     root.destroy() #Закрываем программу (окно)

root = Tk() #Запуск окна программы
root.title("Cryptoup") #Заголовок программы
txt = Text(root,width=40,height=15,font="12") # Формирование текстового окна
txt.pack()# Вывод текстового окна

m = Menu(root) 
root.config(menu=m) 
 
fm = Menu(m) 
m.add_cascade(label="Volume",menu=fm) 
fm.add_command(label="Select file",command=open_vol) 
fm.add_command(label="Mount volume",command=open_vol)
fm.add_command(label="Dismount volume",command=about)
fm.add_command(label="Exit",command=close_win)

pm = Menu(m) #Создание меню
m.add_cascade(label="Help",menu=pm) 
pm.add_command(label="About",command=about) 


 
root.mainloop() 

