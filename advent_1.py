# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:17:45 2020

@author: et140552
"""

# Import necessary packages
import os
import numpy as np
import pandas as pd
import math
import statistics as st
import matplotlib.pyplot as plt
import scipy
from scipy import optimize
import tkinter as tk
from tkinter import *
from tkinter import filedialog
plt.style.use('ggplot')

#%% Open dialog box to select files to be analysed

root = tk.Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",
                                              title = "Advent 1",
                                              filetypes = (("csv files","*.csv"),("all files","*.*")))
files = root.filename
button_exit = Button(root,  
                      text = "Exit", 
                      command = root.destroy)

button_exit.grid(column = 1, row = 1)

root.mainloop()

#%%

lst_of_expenses = pd.read_csv(files,
                              header = None)

lst = lst_of_expenses[0].tolist()

for i, value in enumerate(lst):
    for j, value in enumerate(lst):
        if lst[i] + lst[j] == 2020:
            a = lst[i]
            b = lst[j]

print(a*b)


#%%
for i, value in enumerate(lst):
    for j, value in enumerate(lst):
        for k, value in enumerate(lst):
            if lst[i] + lst[j] + lst[k] == 2020:
                a = lst[i]
                b = lst[j]
                c = lst[k]
                
print(a*b*c)