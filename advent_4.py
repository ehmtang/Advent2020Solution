# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:51:25 2020

Credit from Joey deVilla
https://www.globalnerdy.com/2020/12/06/my-solution-to-advent-of-code-2020s-day-4-challenge-in-python/


refer to why not to iterate over pandas 
https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
https://towardsdatascience.com/you-dont-always-have-to-loop-through-rows-in-pandas-22a970b347ac

@author: et140552
"""
# Import necessary packages
import os

# Get current working directory
dirname = os.path.dirname(os.path.abspath(__file__))
advent_4 = dirname + r'\advent_4.txt'


with open(advent_4) as f:
    data = f.read()
    
split_input = data.split("\n\n")

split_input_2 = [string.replace("\n", " ") for string in split_input]

split_input_3 = [string.split() for string in split_input_2]

def convert_to_dictionary(password_list):
    dictionary = {}
    
    for item in password_list:
        item_parts = item.split(":")
        key = item_parts[0]
        value = item_parts[1]
        dictionary[key] = value
        
    return dictionary

passports = [convert_to_dictionary(item) for item in split_input_3]

def is_valid_passport(passport):
    has_birth_year = "byr" in passport
    has_issue_year = "iyr" in passport
    has_expiration_year = "eyr" in passport
    has_height = "hgt" in passport
    has_hair_color = "hcl" in passport
    has_eye_color = "ecl" in passport
    has_passport_id = "pid" in passport
    has_country_id = "cid" in passport
    
    return (
        has_birth_year and
        has_issue_year and
        has_expiration_year and
        has_height and
        has_hair_color and
        has_eye_color and
        has_passport_id
    )

valid_passports = [passport for passport in passports if is_valid_passport(passport)]
print(len(valid_passports))

def has_valid_values(passport):
    has_valid_birth_year = 1920 <= int(passport["byr"]) <= 2002
    has_valid_issue_year = 2010 <= int(passport["iyr"]) <= 2020
    has_valid_expiration_year = 2020 <= int(passport["eyr"]) <= 2030
    
    has_valid_height = False
    height_units = passport["hgt"][-2:]
    if height_units == "cm":
        height = int(passport["hgt"][:-2])
        has_valid_height = 150 <= height <= 193
    elif height_units == "in":
        height = int(passport["hgt"][:-2])
        has_valid_height = 59 <= height <= 76
        
    def is_valid_hex_string(string):
        test_value = string.lower()
        is_valid = True
 
        for character in string:
            if character not in "0123456789abcdef":
                is_valid = False
                break
 
        return is_valid
        
    has_valid_hair_color = False
    if len(passport["hcl"]) == 7:
        digits = passport["hcl"][1:]
        has_valid_hair_color = is_valid_hex_string(digits)
            
    has_valid_eye_color = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    
    def is_valid_passport_id(value):
        is_valid = False
        
        if len(value) == 9:
            is_valid = True
 
            for character in value:
                if character not in "0123456789":
                    is_valid = False
                    break
        
        return is_valid
    
    has_valid_passport_id = is_valid_passport_id(passport["pid"])
                
        
    return (
        has_valid_birth_year and
        has_valid_issue_year and
        has_valid_expiration_year and
        has_valid_height and
        has_valid_hair_color and
        has_valid_eye_color and
        has_valid_passport_id
    )

truly_valid_passports = [passport for passport in valid_passports if has_valid_values(passport)]
print(len(truly_valid_passports))



