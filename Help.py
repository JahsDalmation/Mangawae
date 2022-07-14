from Data_Checks import *
# The Mangawae Interactive Help Menu!

def InteractiveHelp():

    print('''
[ X ] > # X takes place of the integer corresponding to the option
              you would like to choose! X may be any number that
              is within [ ] for the list of options. Values given
              that are not will not be used, most likely resulting
              in the menu looping.

[ y/n ] > # A simple 'y' or 'n' question. Data (here string) given that
                is not 'y' or 'n' will not be used, most likely resulting
                in the menu looping.

[ EP 1 - # ] > # In this line, # will be the number of the final chapter.
[ EP 1 - X ] > #    The above line is asking for the begging episode.
                    Whereas the bottom line, the final episode, X will
                    be replaced with the given value. Values must be integers
                    and within the range given
''')

    Practicing = True
    while Practicing:
        print('[ 0 ] [ Choose ]')
        print('[ 1 ] [ One ]')
        print('[ 2 ] [ Of ]')
        print('[ 3 ] [ These! ]')
        integer = input('[ X ] > ')
        valid = MenuCheck(integer, 4)
        if valid:
            print('Well Done!')
            Practicing = False

    Practicing = True
    while Practicing:
        print('Do you agree?')
        YN = input('[ y/n ] > ')
        if YN == 'y':
            print('Well Done!')
            Practicing = False
        if YN == 'n':
            print('Well Done!')
            Practicing = False

    Practicing = True
    while Practicing:
        integer1 = input('[ EP 1 - 100 ] > ')
        valid = MenuCheck(integer1, 101)
        if valid:
            print('Well Done!')
            Practicing = False

    Practicing = True
    while Practicing:
        integer2 = input('[ EP %s - X ] > ' % integer1)
        valid = MenuCheck(integer2, 101)
        if valid:
            print('Well Done!')
            Practicing = False

