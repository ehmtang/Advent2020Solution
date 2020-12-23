# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:51:25 2020

@author: et140552
"""
# Import necessary packages
import os

# Get current working directory
dirname = os.path.dirname(os.path.abspath(__file__))
advent_5 = dirname + r'\advent_5.txt'


with open(advent_5) as f:
    data = f.read()
    
data = data.split("\n")

start = 0
end = 128


number_of_rows = list(range(start, end))

boarding_pass = data[0]

def check_row_number(boarding_pass):
    row_start = 0
    row_end = 128
    seat_start = 0
    seat_end = 8
    for region in boarding_pass:
        #print(region)
    
        if region == "F":
            mid_point = (row_start + row_end) / 2
            row_end = mid_point
            # print(row_start, row_end)
        
        elif region == "B":
            mid_point = (row_start + row_end) / 2
            row_start = mid_point
            # print(row_start, row_end)
        
        if region == "L":
            mid_point = (seat_start + seat_end) / 2
            seat_end = mid_point
            # print(seat_start, seat_end)
        
        elif region == "R":
            mid_point = (seat_start + seat_end) / 2
            seat_start = mid_point
            # print(seat_start, seat_end)
    
    return int(row_start*8 + seat_start)

boarding_pass_id = [check_row_number(boarding_pass) for boarding_pass in data]
print(max(boarding_pass_id))
    
# %%
rangeofpasses = list(range(min(boarding_pass_id), max(boarding_pass_id) + 1))

find_my_boarding_pass = [x for x in rangeofpasses if x not in boarding_pass_id]









