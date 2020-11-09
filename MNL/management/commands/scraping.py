from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from MNL.models import Anime
from jikanpy import Jikan

class Command(BaseCommand):
    help = "collect jobs"
    # define logic of command
    def handle(self, *args, **options):
        links = []
        jikan = Jikan()

        driver = webdriver.Chrome("C:/Users/AFIF/Downloads/chromedriver_win32/chromedriver.exe")

        # driver = webdriver.Chrome()
        url= "https://www.justwatch.com/in/provider/netflix/tv-shows?genres=ani&sort_by=release_year"
        driver.maximize_window()
        driver.get(url)
        time.sleep(5)
        count = 0
        #Scrolling _____________________________________________________________________
        from selenium.webdriver.common.action_chains import ActionChains
        i = 1
        for i in range(15):
            ActionChains(driver).move_to_element(driver.find_element_by_class_name('jw-app-footer__link')).perform()
            time.sleep(1.5)
            content = driver.page_source.encode('utf-8').strip()
            soup1 = BeautifulSoup(content,"html.parser")
            anime1 = soup1.find_all( class_="title-list-grid__item")
            for div in anime1:
                links.append(div.a['href'])
                l = []
                l = div.a['href'].split('/')
                l2 = []
                l2 = l[3].split('-')
                s = ""
                for i in l2:
                    s += i
                    s += " "
                # try:
                # save in db
                if Anime.objects.filter(anime_name=s).exists():
                    print("{} contained in queryset".format(s))
                else:
                    try:

                        search_result = jikan.search('anime', s)
                        p = Anime(anime_name = s, score = search_result['results'][0]['score'],synopsis = search_result['results'][0]['synopsis'], url = search_result['results'][0]['url'], image_url = search_result['results'][0]['image_url'])
                        p.save()
                        print('%s added' % (s))
                        count +=1
                    except:
                        print("{} COULD NOT BE ADDED".format(s))

                    time.sleep(4)                    
        print(count)
        # print(AnimeNames.objects.get(anime_name='ergo proxy'))
        driver.quit()
            
        self.stdout.write( 'job complete' )

