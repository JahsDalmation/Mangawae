#!/usr/bin/env python3

from os.path import expanduser
from subprocess import Popen, PIPE, run
from Data_Checks import MenuCheck

# Mangwaae manga browser!

# Define the Browser class of functions!
class Browser:
##

    # Define the initial function to be called alongside, Browser.
    def __init__(self):
    ##

        # Define the Home for the user,
        #   and assign it, as a variable to self.
        self.Home = expanduser('~')
        ##

    # Define the function ListManga & arguments.
    def ListManga(self):

        # Run the ls cmd on the $HOME/Manga directory.
        LsManga = Popen(['ls', '%s/Manga/' % self.Home], text=True, stdout=PIPE)
        ##

        #   Capture the results of LsManga through stdout.
        #       Assigning to output to the Output variable.
        Output = LsManga.communicate()
        ##

        # Filter only the ls results from the Output variable/stdout PIPE.
        LsOutput = Output[0]
        ##

        # Split the contents, of LsOutput, into a list.
        MangaList = LsOutput.split('\n')
        ##

        # Remove unwanted items (directories) from the MangaList list.
        #   Such as the tmp dir. (It is just used to download jpg's)
        MangaList.remove('tmp')
        MangaList.remove('')
        ##

        # Create a simple counter and for loop.
        #   Looping for every item/Manga in the list, MangaList.
        #   Every pass, increase the value of the counter by 1.
        MangaCount = 0
        for Manga in MangaList:
            print('[ %s ] [ %s ]' % (MangaCount, Manga))
            MangaCount += 1
        ##

        # Return the list, MangaList.
        return MangaList
        ##
    ##

    # Define the function ChooseManga & arguments.
    def ChooseManga(self, MangaList):

        # Define the varible Choosing as True.
        Choosing = True
        ##

        # Create a while loop, looping on the criteria that
        #   Choosing is True.
        while Choosing:

            # Ask the user to input the value corresponding
            #   to the manga they wish to read.
            ChosenManga = input('[ X ] > ')
            ##

            # Define the variable, valid, as the result of
            #   the function, MenuCheck, being called to assess
            #   the 'validity' of ChosenManga's value.
            valid = MenuCheck(ChosenManga, len(MangaList))
            ##

            # If MenuCheck returns True, and thus valid is True.
            if valid:

                # Change the value of the Choosing variable to False,
                #   ending the loop started earlier.
                Choosing = False
                ##

                # Now that ChosenManga has been proven to be an
                #   acceptable value, return it.
                return ChosenManga
                ##
            ##
        ##
    ##

    # Define the function ChooseChapter & arguments
    def ChooseChapter(self, Manga):
        LsChapters = Popen(['ls', '%s/Manga/%s/' % (self.Home, Manga)],
                           text=True,
                           stdout=PIPE)

        Output = LsChapters.communicate()

        LsOutput = Output[0]

        ChapterList = LsOutput.split('\n')
        ChapterList.remove('')

        Choosing = True
        while Choosing:
            ChosenChapter = input('[ Ch: %s-%s ] > ' % (1, len(ChapterList)))
            valid = MenuCheck(ChosenChapter, len(ChapterList) + 1)
            if valid:
                Choosing = False
                return ChosenChapter

    # Define the function ReadManga & arguments.
    def ReadManga(self, Manga, ChosenChapter):

        # From the li
        #run(['zathura %s/Manga/%s/%s.pdf' % (self.Home, Manga, ChosenChapter)],
        run(['atril %s/Manga/%s/%s.pdf' % (self.Home, Manga, ChosenChapter)],
              shell=True)
    ##

    def Menu(self):

        Modes = [
            'Next',
            'Previous',
            'Back']

        ModeCounter = 0
        for mode in Modes:
            print('[ %s ] [ %s ]' % (ModeCounter, mode))
            ModeCounter += 1

        Choosing = True
        while Choosing:
            Mode = input('[ X ] > ')
            valid = MenuCheck(Mode, ModeCounter)
            if valid:
                Choosing = False
                LocalMode = Modes[int(Mode)]
                return LocalMode
