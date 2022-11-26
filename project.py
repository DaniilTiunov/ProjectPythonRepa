import pandas as pd
from openpyxl import Workbook


wb = Workbook()
df = pd.read_excel('439_2frem.xls', engine = 'openpyxl')




type(df)