import pandas as pd
import tkinter as tk
from tkinter import *
import numpy as np
from openpyxl import Workbook

datatable = pd.read_excel('439_2frem.xls')

window = tk.Tk()
window.title('Table')
label = Label(window, text = datatable)
label.grid(column = 0, row = 0)







window.mainloop()



