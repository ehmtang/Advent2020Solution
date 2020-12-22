# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:51:25 2020

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

import ast

# Get current working directory
dirname = os.path.dirname(os.path.abspath(__file__))
advent_4 = dirname + r'\advent_4.txt'


#Line Formatter

test = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""






RUN_TEST = False
TEST_SOLUTION = 2
TEST_INPUT_FILE = 'test_input_day_04.txt'
INPUT_FILE = 'input_day_04.txt'

PASSPORT_FIELDS = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
}

REQUIRED_PP_FIELDS = PASSPORT_FIELDS.difference({'cid'})


ARGS = [REQUIRED_PP_FIELDS, ]

with open(advent_4) as f:
    data = f.read()
    
    
# Separate the each 
passports_lines = data.split("\n\n")
fields_lines = []

for i in range(len(passports_lines)):
    temp = passports_lines[i].replace("\n", " ")
    fields_lines.append(temp)

for i in range(len(fields_lines)):
    fields_lines[i]=fields_lines[i].replace(" ", "', ")
    fields_lines[i]=fields_lines[i].replace(":", "':'")

        
        
        
        
        
        
        
        

#%%

print(blah[0])
thisdict = {blah[0]}

# %%
def valid_passports(input):
    """
    Function to count valid passports, Advent of Code Day 4 Challenge!
    """

    import ast

    prelim = input.split("\n\n")

    def clean(trash):
        """
        Cleanup entries on list for unwanted characters.
        """

        trash = trash.replace("\n", " ")
        trash = trash.replace(":", "':'")
        trash = trash.replace(" ", "', '")

        return trash

    prelim2 = [clean(x) for x in prelim]

    insert_quotation = lambda string: string + "'}"

    insert_curly = lambda string: "{'" + string

    prelim3 = [insert_quotation(x) for x in prelim2]

    prelim4 = [insert_curly(x) for x in prelim3]
    print(prelim4)

    df = pd.DataFrame([ast.literal_eval(x) for x in prelim4])

    df = df.drop(columns=["cid"])

    return df.dropna()


with open(advent_4) as f:
    part1 = f.read()


df = valid_passports(part1[:-1])

df = df.astype({"byr": int, "eyr": int, "iyr": int})

df = df[(1920 <= df.byr) & (df.byr <= 2002)]
df = df[(2010 <= df.iyr) & (df.byr <= 2020)]
df = df[(2020 <= df.eyr) & (df.eyr <= 2030)]

for x in df.hgt:
    #contain cm
    x = 
    
# check if "cm" or "in" is in list
# back two [:-2] create new list as int
    # check new list is between 150 and 193 cm
    # check new list is between 59 and 76 in

# check '#' is == [0] true  else fail
# check character 0-9 or a-f
# ecl in list [amb blu brn gry grn hzl oth]
# pid is len(x) == 9 and is a number
# first character is 0

























