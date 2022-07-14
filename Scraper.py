<<<<<<< HEAD
from Data_Checks import *
=======
>>>>>>> 7519a2c (Initial import of program files!)
import subprocess
import requests
from bs4 import BeautifulSoup

class MangaSearch:

    # Define the init 'magic-method'. This function will be 'called' each time 
    #   MangaSearch() is 'init'alized! The method takes 3 arguments;
    #
    #   self (The object the method is called on),
    #
    #   search_type (The 'critera' on how results will be gathered),
    #       which defaults to: 'newest',
    #
    #   search_query (String to search for, used when search_type='search'),
    #       which defaults to: '' (Ensures all arguments are met).
    #

    def __init__(self):

        # Print a nice warm welcome message to the MangaSearch class :)
        welcome = 'What Manga would you like to read today?'
        welcome_wrap = '-' * len(welcome)
        print('%s\n%s\n%s\n' % (welcome_wrap, welcome, welcome_wrap))

    def scrape_searcher(self, search_type, search_query):

        # If the search_type argument is not 'search' do:
        if search_type != 'search':

            # Link 'base' for a genre based search.
            link_base = 'https://manganato.com/genre-all'
            if search_type == 'newest':
                # Assign the argument/object self
                link = '%s?type=newest' % link_base
            if search_type == 'hottest':
                link = '%s?type=topview' % link_base
            if search_type == 'latest':
                link = link_base

            scrape = requests.get(link).text
            html = BeautifulSoup(scrape, 'lxml')
            manga_block = html.find('div', class_='panel-content-genres')
            results = manga_block.find_all('a', 
                class_='genres-item-name text-nowrap a-h')
            Error = False

        if search_type == 'search':

            link_base = 'https://manganato.com/search/story/'
            self.link = str('%s%s' % (link_base, search_query))
            scrape = requests.get(self.link).text 
            html = BeautifulSoup(scrape, 'lxml')
            manga_blocks = html.find('div', class_='panel-search-story')
            try:
                results = manga_blocks.find_all('a',
                                                class_="a-h text-nowrap item-title")
                Error = False
            except AttributeError:
                Error = True

        if Error != True:
            counter = 0
            x = 0
            print()
            for manga in results:
                if x < 10:
                    print('[ %s ] [ %s ]' %
                          (counter,
                           manga.text,
                           ))
                    counter += 1
                x += 1
            return results
        elif Error:
            return ''
            results = manga_blocks.find_all('a',
                class_="a-h text-nowrap item-title")

        counter = 0
        x = 0
        print()
        for manga in results:
            if x < 5:
                print('[ %s ] [ %s ]' % 
                    (counter, 
                    manga.text, 
                    ))
                counter += 1
            x += 1
        return results

    def manga_details(self, manga_link):
        scrape = requests.get(manga_link).text
        html = BeautifulSoup(scrape, 'lxml')
        info_panel = html.find('div', class_='panel-story-info')
        panel_values = info_panel.find_all('td', class_='table-value')
        author = panel_values[1].text.replace('\n','')
        status = panel_values[2].text
        genres = panel_values[3].find_all('a')
        genre = ''
        x = 0
        for i in genres:
            if x == 0:
                genre = genre + '%s' % i.text
            if x > 0:
                genre = genre + '-%s' % i.text
            x += 1
        panel_values_2 = info_panel.find('div', 
            class_='story-info-right-extent')

        panel_values_2_data = panel_values_2.find_all('span', 
            class_='stre-value')

        updated = panel_values_2_data[0].text
        views = panel_values_2_data[1].text
        stars = panel_values_2_data[2].parent.next_sibling.next_sibling.find('em',
            property='v:average').text

        description = info_panel.find('div', 
            class_='panel-story-info-description').text.replace('Description :\n'
                ,'')

        print('''
[ Author  ] [ %s ]
[ Status  ] [ %s ]
[ Genre/s ] [ %s ]
[ Updated ] [ %s ]
[ Views   ] [ %s ]
[ Rating  ] [ %s/5 ]
%s
''' % (author, status, genre, updated, views, stars, description))


    def menu(self):

        modes = ['newest',
            'hottest',
            'latest',
            'search',
            'back',
            'quit',
            ]

        mode_counter = 0
        print()
        for mode in modes:
            print('[ %s ] [ %s ]' % (mode_counter, modes[mode_counter]))
            mode_counter += 1

        Choosing = True
        while Choosing:
            mode = input('[ X ] > ')
            valid = MenuCheck(mode, mode_counter)
            if valid:
                Choosing = False
        return modes[int(mode)]
        print()
        
    def manga_download(self, link, title):
        scrape = requests.get(link).text 
        html = BeautifulSoup(scrape, 'lxml')
        chapter_list = html.find('div', class_='panel-story-chapter-list')

        if chapter_list == None:
            print('Sorry the manga you have chosen does not seem to have any chapters!')
            print('Here is the link just incase: [ %s ]' % link)

        if chapter_list != None:
            chapters = chapter_list.find_all('a', class_='chapter-name text-nowrap')

            chapter_count = 0
            for chapter in chapters:
                chapter_count += 1


            Choosing = True
            while Choosing:
                chosen_chapter = input('[ EP: 1 - %s ] > ' % chapter_count)
                valid = MenuCheck(chosen_chapter, (chapter_count + 1))
                if valid:
                    Choosing = False

            Choosing = True
            while Choosing:
                final_chapter = input('[ EP: %s -> X ] > ' % chosen_chapter)
                valid = MenuCheck(final_chapter, (chapter_count + 1))
                if valid:
                    Choosing = False

            while int(chosen_chapter) <= int(final_chapter):

                chapter_link = chapters[chapter_count - int(chosen_chapter)]['href']
                chapter_scrape = requests.get(chapter_link).text
                chapter_html = BeautifulSoup(chapter_scrape, 'lxml')
                chapter_pages = chapter_html.find('div', class_='container-chapter-reader')
                pages = chapter_pages.find_all('img')

                page_counter = 1
                for page in pages:
                    if page_counter < 10:
                        Po = '00%s' % page_counter
                    if page_counter < 100 and page_counter >= 10:
                        Po = '0%s' % page_counter
                    if page_counter >= 1000:
                        Po = '%s' % page_counter
                    subprocess.run(["curl --silent --create-dirs --header 'Referer: https://readmanganato.com/' --output '/home/ghost/Manga/tmp/%s.jpg' '%s'" % (Po, page['src'])], shell=True)
                    page_counter += 1
        
                subprocess.run(['mkdir ~/Manga/%s/' % title.replace(' ','-')],
                               shell=True)
                subprocess.run(['img2pdf ~/Manga/tmp/*.jpg --output ~/Manga/%s/%s.pdf'
                                % (title.replace(' ','-'), chosen_chapter)], shell=True)
                subprocess.run(["rm -rf ~/Manga/tmp/*"], shell=True)

                chosen_chapter = int(chosen_chapter)
                chosen_chapter += 1
