# Main Menu - Mangawae!
from Data_Checks import *

def Main_Menu():
    modes = ['Local', 'External', 'Quit']

    mode_count = 0
    for mode in modes:
        print('[ %s ] > [ %s ]' % (mode_count, mode))    
        mode_count += 1

    User_Mode = input('[ X ] > ')

    menu = int_check(User_Mode)
    if menu is False:
        print('FYM')
        return False
    menu = range_check(User_Mode, 0, mode_count)
    if menu is False:
        print('FYM')
        return False
    elif menu:
        Mode = modes[int(User_Mode)]
        print(Mode)
        return Mode

No = True
while No:
    Main_Menu()
