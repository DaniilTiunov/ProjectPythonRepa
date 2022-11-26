#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

tabla = pd.read_excel('balance.xlsx')


# In[2]:


print(tabla['Период'])
print(tabla['Основные средства'])
print(tabla['Запасы'])


# In[3]:


x = tabla['Период']
y = tabla['Основные средства']
z = tabla['Запасы']
plt.grid()
plt.show
plt.plot(x, y)
plt.plot(x, z)


# In[ ]:




