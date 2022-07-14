# Main Menu - Mangawae!
from Data_Checks import *

def Main_Menu():
<<<<<<< HEAD

    # Loop the Main Menu to ensure that a mode is chosen succesfully
    #   before the function ends.
    Deciding = True
    while Deciding:

    # Define the avaliable modes.
        modes = ['Local', 'External', 'Help', 'Quit']

    # Print out the avaliable modes, with a coresponding
    #   counter. This allows the user to view the avaliable modes
    #   aswell as choose a specific one, using the mode_count.
    #       The mode_count variable will align to the position
    #       of the mode in the modes list (defined above).
        mode_count = 0
        for mode in modes:
            print('[ %s ] > [ %s ]' % (mode_count, mode))
            mode_count += 1

    # Ask the user for the mode they wish to use.
    #   This should be a number that corresponds to the mode_count
    #   of the mode they wish to use.
        User_Mode = input('[ X ] > ')

    # Run both an integer check and range check,
    #   this ensures that the data given by the user
    #   is usable by the program and will not return
    #   an error.
        valid = MenuCheck(User_Mode, mode_count)
        if valid:
            Mode = modes[int(User_Mode)]
            Deciding = False
            return Mode

        #menu = int_check(User_Mode)
        #if menu is False:
            #print('The value is not an integer')
        #elif menu:
            #menu = range_check(User_Mode, 0, mode_count)
            #if menu is False:
                #print('The value does not meet 0 <= value <= %s' % mode_count)
            #if menu:
                #Mode = modes[int(User_Mode)]
                #Deciding = False
                #return Mode
=======
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
>>>>>>> 7519a2c (Initial import of program files!)
