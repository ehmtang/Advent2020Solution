# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:20:08 2020

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
                                              title = "Advent 2",
                                              filetypes = (("csv files","*.csv"),("all files","*.*")))
files = root.filename
button_exit = Button(root,  
                      text = "Exit", 
                      command = root.destroy)

button_exit.grid(column = 1, row = 1)

root.mainloop()

def tolerance():
    lower_tolerance = #first number
    upper_tolerance = #second number
    character = #character to be parsed
    count = character in StringVar
    if count between lower and upper tolerance :
        True
    elif
        FALSE
        