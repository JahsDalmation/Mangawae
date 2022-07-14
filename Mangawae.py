from Scraper import *
from Data_Checks import *
<<<<<<< HEAD
from Main_Menu import *
from Help import InteractiveHelp

MangaSearch = MangaSearch()
Mangaing = True
while Mangaing:
    Mode = Main_Menu()

### LOCAL MODE BLOCK ###
    if Mode == 'Local':
        print('Keeping it local!')
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
=======

Browsing = True
while Browsing:
    Main_Menu()

    manga_search = MangaSearch()

    Mangaing = True
    while Mangaing:

        search_query = ''
        search_type = manga_search.menu()
        if search_type == 'quit':
            exit()
        if search_type == 'search':
            search_query = manga_search.search_query() 
        search_results = manga_search.scrape_searcher(search_type, search_query)
        chosen_manga = input('[ X ] > ')
        manga_search.manga_details(search_results[int(chosen_manga)]['href'])
        download = input('[ y/n ] > ')
        if download == 'y':
            manga_search.manga_download(search_results[int(chosen_manga)]['href'],
                search_results[int(chosen_manga)].text)
        elif download == 'n':
            Mangaing = True
        else:
            print('sorry try again')
>>>>>>> 7519a2c (Initial import of program files!)
