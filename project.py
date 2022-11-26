import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import numpy as np
from openpyxl import Workbook

datatable = pd.read_excel('439_2frem.xls')

window = tk.Tk()                                                 
window.geometry("700x400")
window.title('Приложение для расчета показателей инвестиционного анализа предприятия')

frame1 = tk.LabelFrame(window)                                       # фрейм для создания ещё трёх кнопок :\
frame1.place(height = 250, width = 370, rely = 0.03, relx = 0.45)
button_frame = tk.Button(frame1, text = "Календарный план")
button_frame.place(rely = 0.03, relx = 0.3, height = 50, width = 200)

button_frame2 = tk.Button(frame1, text = "Ресурсы")
button_frame2.place(rely = 0.39, relx = 0.3, height = 50, width = 200)

button_frame3 = tk.Button(frame1, text = "Список активов")
button_frame3.place(rely = 0.75, relx = 0.3, height = 50, width = 200)

button1 = tk.Button(window, text = "Проект")            #FUCKING BUTTONS 
button1.place(rely = 0.03, relx = 0.01, width=300)

button2 = tk.Button(window, text = "Компания")
button2.place(rely = 0.1, relx = 0.01, width=300)

button3 = tk.Button(window, text = "Окржуение")
button3.place(rely = 0.17, relx = 0.01, width=300)

button4 = tk.Button(window, text = "Инвестиционный план")
button4.place(rely = 0.24, relx = 0.01, width=300)

button5 = tk.Button(window, text = "Операционный план")
button5.place(rely = 0.31, relx = 0.01, width=300)

button6 = tk.Button(window, text = "Финансирование")
button6.place(rely = 0.38, relx = 0.01, width=300)

button7 = tk.Button(window, text = "Результаты")
button7.place(rely = 0.45, relx = 0.01, width=300)

button8 = tk.Button(window, text = "Анализ проекта")
button8.place(rely = 0.52, relx = 0.01, width=300)

button9 = tk.Button(window, text = "Актуализация")
button9.place(rely = 0.59, relx = 0.01, width=300)   #конец кнопок :)

window.mainloop()



