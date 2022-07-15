from Scraper import *
from Data_Checks import *
from Main_Menu import *
from Help import InteractiveHelp
from os.path import expanduser
from subprocess import Popen, PIPE, run
from Browser import *

MangaSearch = MangaSearch()
Mangaing = True
while Mangaing:
    Mode = Main_Menu()

### LOCAL MODE BLOCK ###
    if Mode == 'Local':

        Local = Browser()

        MangaList = Local.ListManga()

        ChosenManga = Local.ChooseManga(MangaList)

        Manga = MangaList[int(ChosenManga)]

        ChosenChapter = Local.ChooseChapter(Manga)

        ChosenChapter = int(ChosenChapter)
        Reading = True
        while Reading:
            Local.ReadManga(Manga, ChosenChapter)

            mode = Local.Menu()
            if mode == 'Next':
                ChosenChapter += 1
            if mode == 'Previous':
                ChosenChapter -= 1
            if mode == 'Back':
                Reading = False

### LOCAL MODE BLOCK ###

### EXTERNAL MODE BLOCK ###
    if Mode == 'External':
        Browsing = True
        while Browsing:
            search_query = ''
            search_type = MangaSearch.menu()

            if search_type != 'back':
                if search_type == 'search':
                    Searching = True
                    while Searching:
                        search_query = input('[ manga ] > ')
                        search_results = MangaSearch.scrape_searcher(search_type, search_query)
                        if search_results != '':
                            Searching = False
                elif search_type != 'search':
                    search_results = MangaSearch.scrape_searcher(search_type, search_query)
                result_counter = 9
                print('[ %s ] [ back ]' % (result_counter + 1))

                Choosing = True
                while Choosing:
                    chosen_manga = input('[ X ] > ')
                    valid = MenuCheck(chosen_manga, result_counter + 2)

                    if valid:
                        Choosing = False
                        if int(chosen_manga) == (result_counter + 1):
                            Continue = False
                        else:
                            Continue = True

                if Continue:
                    MangaSearch.manga_details(search_results[int(chosen_manga)]['href'])

                    Choosing = True
                    while Choosing:
                        download = input('[ y/n ]')

                        if download == 'y':
                            MangaSearch.manga_download(search_results[int(chosen_manga)]['href'],
                                                   search_results[int(chosen_manga)].text)
                            Choosing = False

                        if download == 'n':
                            Choosing = False
                        elif download != 'y' and download != 'n':
                            print('Please enter y or n')

            elif search_type == 'back':
                Browsing = False
### EXTERNAL MODE BLOCK ###

### HELP MODE BLOCK ###
    if Mode == 'Help':
        InteractiveHelp()
### HELP MODE BLOCK ###

### QUIT MODE BLOCK ###
    if Mode == 'Quit':
        Mangaing = False
### QUIT MODE BLOCK ###
