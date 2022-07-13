from Scraper import *
from Data_Checks import *

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
