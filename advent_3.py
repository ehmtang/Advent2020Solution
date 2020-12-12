# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:25:28 2020

@author: EHMTang
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
advent_3 = dirname + r'\advent_3.txt'

# Get directory of 'data' to be imported
df = pd.read_csv(advent_3,
                 header=None)


def is_tree_at_coordinates(hill_x, hill_y):
    map_x = hill_x % 31
    return df[0][hill_y][map_x] == "#"


print(is_tree_at_coordinates(32, 0))


#%%

def tree_count_for_slope(right_increment, down_increment):
    right_coordinate = 0
    down_coordinate = 0
    tree_count = 0
 
    while down_coordinate < len(df):
        if is_tree_at_coordinates(right_coordinate, down_coordinate):
            tree_count += 1
        right_coordinate += right_increment
        down_coordinate += down_increment
 
    return tree_count

a = tree_count_for_slope(1,1)
b = tree_count_for_slope(3,1)
c = tree_count_for_slope(5,1)
d = tree_count_for_slope(7,1)
e = tree_count_for_slope(1,2)

f = a*b*c*d*e



 