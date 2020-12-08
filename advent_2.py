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



# Get current working directory
dirname = os.path.dirname(os.path.abspath(__file__))
advent_2 = dirname + r'\advent_2.txt'

# Get directory of 'data' to be imported
F = pd.read_csv(advent_2,
                header=None,
                delimiter=' ')

# new data frame with split value columns 
new = F[0].str.split('-', n = 1, expand = True) 
  
# making separate first name column from new data frame 
F['LowerTol']= new[0].astype(int)
  
# making separate last name column from new data frame 
F['UpperTol']= new[1].astype(int) 
  
# Dropping old Name columns 
F.drop(columns =[0], inplace = True)

F[1] = F[1].str.replace(':', '').astype(str)


#%%

condion =[]
for i in range(len(F)):
    counter = F[2][i].count(str(F[1][i]))
    if counter >= F['LowerTol'] && counter <= F['UpperTol']