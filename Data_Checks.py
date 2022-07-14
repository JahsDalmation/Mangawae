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
<<<<<<< HEAD
    if min_value <= int(data) < max_value:
        return True
    if min_value > int(data) or int(data) >= max_value:
        return False

#######################
# Int And Range Check
#######################
def MenuCheck(data, max_value):
    valid = int_check(data)
    if valid is False:
        print('The value is not an integer')
    elif valid:
        valid = range_check(data, 0, max_value)
        if valid is False:
            print('The value does not meet 0 <= value < %s' % max_value)
        elif valid:
            return True
=======
    if min_value <= int(data) <= max_value: 
        return True
    elif min_value > int(data) or int(data) > max_value:
        return False

#######################
>>>>>>> 7519a2c (Initial import of program files!)
