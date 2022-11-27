import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from tkinter.filedialog import asksaveasfilename
import numpy as np
from openpyxl import Workbook

datatable = pd.read_excel('439_2frem.xls')

window = tk.Tk()                                                 
window.geometry("700x400")
window.title('Приложение для расчета показателей инвестиционного анализа предприятия')
window.resizable(False, False)
window.config(bg='black', )                                       # отключает возможность растягивать окно как хочется

frame1 = tk.LabelFrame(window)  
frame1.config(bg='grey20', )                                      # фрейм для создания ещё трёх кнопок :\
frame1.place(height = 250, width = 370, rely = 0.03, relx = 0.45)

def button_Click():                     #Функция создания окна для кнопок(временная)
    window = Tk()
    window.title(Text)
    window.geometry("700x400")



k = 0

def Plan():
    button_frame = tk.Button(frame1, text = "Календарный план", bg='grey30', 
    fg='white', activebackground="grey10", activeforeground="white", command = button_Click)
    button_frame.place(rely = 0.04, relx = 0.25, height = 50, width = 200,)
    button_frame.bind('<Enter>', on_enter_frame)
    button_frame.bind('<Leave>', on_leave_frame)

    button_frame2 = tk.Button(frame1, text = "Ресурсы", bg='grey30', 
    fg='white', activebackground="grey10", activeforeground="white", command = button_Click)
    button_frame2.place(rely = 0.4, relx = 0.25, height = 50, width = 200)
    button_frame2.bind('<Enter>', on_enter_frame)
    button_frame2.bind('<Leave>', on_leave_frame)

    button_frame3 = tk.Button(frame1, text = "Список активов", bg='grey30', 
    fg='white', activebackground="grey10", activeforeground="white", command = listActive)
    button_frame3.place(rely = 0.76, relx = 0.25, height = 50, width = 200)
    button_frame3.bind('<Enter>', on_enter_frame)
    button_frame3.bind('<Leave>', on_leave_frame)

def buttonPlan():
    global k
    if (k==0):
        k = 1 
        Plan()
    elif(k==1):
        k=0
        for widgets in frame1.winfo_children():
            widgets.destroy()

def listActive():

    def save_file():
        filepath = asksaveasfilename(defaultextension = "txt", filetypes = [("Текстовые файлы", "*.txt")])
        if not filepath:
            return
        with open(filepath, "w", encoding = "UTF-8") as output_file:
            text = text_edit.get("1.0", tk.END)
            output_file.write(text)
        window3.title(f"Work with - {filepath}")

    window3 = Tk()
    window3.title(Text)
    window3.geometry("700x400")
    
    buttonClose = tk.Button(window3, text = "Закрыть",  command = window3.destroy)  # Создание кнопок
    buttonClose.place(rely = 0.4, relx = 0.8, height = 20, width = 90)
    
    buttonQuest = tk.Button(window3, text = "Справка")
    buttonQuest.place(rely = 0.3, relx = 0.8, height = 20, width = 90)
    
    buttonRead = tk.Button(window3, text = "Редактировать")
    buttonRead.place(rely = 0.2, relx = 0.8, height = 20, width = 90)

    buttonRead = tk.Button(window3, text = "Cохранить", command = save_file)
    buttonRead.place(rely = 0.1, relx = 0.8, height = 20, width = 90)
    
    activList = tk.Label(window3, text = "Список активов: ")
    activList.pack(anchor = NW)
    
    text_edit = tk.Text(window3, width=20, height=30)        #Создание многострочного поля ввода
    text_edit.pack(side=LEFT)
    
    
    window3.mainloop()
    

def on_enter_frame(e):
    e.widget['background'] = 'grey40'
def on_leave_frame(e):
    e.widget['background'] = 'grey30'
def on_enter_win(e):
    e.widget['background'] = 'grey40'
def on_leave_win(e):
    e.widget['background'] = 'grey20'


buttonBrowse = tk.Button(window, text = 'Обзор', bg='grey20', 
fg='white', activebackground="grey10", activeforeground="white", command = button_Click)
buttonBrowse.place(rely = 0.8, relx = 0.8, height='35', width=120)
buttonBrowse.bind('<Enter>', on_enter_win)
buttonBrowse.bind('<Leave>', on_leave_win)

button1 = tk.Button(window, text = "Проект", bg='grey20', 
    fg='white', activebackground="grey10", activeforeground="white", command = button_Click)            #FUCKING BUTTONS 
button1.place(rely = 0.04, relx = 0.01, height='35', width=300)
button1.bind('<Enter>', on_enter_win)
button1.bind('<Leave>', on_leave_win)

button2 = tk.Button(window, text = "Компания", bg='grey20', 
    fg='white', activebackground="grey10", activeforeground="white", command = button_Click)
button2.place(rely = 0.14, relx = 0.01, height='35', width=300)
button2.bind('<Enter>', on_enter_win)
button2.bind('<Leave>', on_leave_win)

button3 = tk.Button(window, text = "Окржуение", bg='grey20', 
    fg='white', activebackground="grey10", activeforeground="white", command = button_Click)
button3.place(rely = 0.24, relx = 0.01, height='35', width=300)
button3.bind('<Enter>', on_enter_win)
button3.bind('<Leave>', on_leave_win)


button4 = tk.Button(window, text = "Инвестиционный план", bg='grey20', 
    fg='white', activebackground="grey10", activeforeground="white", command = buttonPlan)
button4.place(rely = 0.34, relx = 0.01, height='35', width=300)
button4.bind('<Enter>', on_enter_win)
button4.bind('<Leave>', on_leave_win)

button5 = tk.Button(window, text = "Операционный план", bg='grey20',   
    fg='white', activebackground="grey10", activeforeground="white", command = button_Click)
button5.place(rely = 0.44, relx = 0.01, height='35', width=300)
button5.bind('<Enter>', on_enter_win)
button5.bind('<Leave>', on_leave_win)

button6 = tk.Button(window, text = "Финансирование", bg='grey20', 
    fg='white', activebackground="grey10", activeforeground="white", command = button_Click)
button6.place(rely = 0.54, relx = 0.01, height='35', width=300)
button6.bind('<Enter>', on_enter_win)
button6.bind('<Leave>', on_leave_win)

button7 = tk.Button(window, text = "Результаты", bg='grey20', 
    fg='white', activebackground="grey10", activeforeground="white", command = button_Click)
button7.place(rely = 0.64, relx = 0.01, height='35', width=300)
button7.bind('<Enter>', on_enter_win)
button7.bind('<Leave>', on_leave_win)

button8 = tk.Button(window, text = "Анализ проекта", bg='grey20', 
    fg='white', activebackground="grey10", activeforeground="white", command = button_Click)
button8.place(rely = 0.74, relx = 0.01, height='35', width=300)
button8.bind('<Enter>', on_enter_win)
button8.bind('<Leave>', on_leave_win)

button9 = tk.Button(window, text = "Актуализация", bg='grey20', 
    fg='white', activebackground="grey10", activeforeground="white", command = button_Click)
button9.place(rely = 0.84, relx = 0.01, height='35', width=300)   
button9.bind('<Enter>', on_enter_win)
button9.bind('<Leave>', on_leave_win)                                               #конец кнопок :)


window.mainloop()



