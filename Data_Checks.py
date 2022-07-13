#!/usr/bin/python

#######################
#Integer Check & Proof
#######################
def int_check(data):
    try:
        data = int(data)
        return True
    except ValueError:
        return False

#######################
# Range Check & Proof
#######################
def range_check(data, min_value, max_value):
    if min_value <= int(data) <= max_value: 
        return True
    elif min_value > int(data) or int(data) > max_value:
        return False

#######################
