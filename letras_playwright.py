from playwright.sync_api import sync_playwright

import time
import random
import save_letras as sl

import requests
import pandas as pd
from bs4 import BeautifulSoup

invisible_browser = False

def dibra_time(sec):
    delay = random.random()*sec
    time.sleep(delay)

def find_genres():
    res = requests.get('https://www.letras.mus.br/estilos/')
    print("The status code is ", res.status_code)
    soup_data = BeautifulSoup(res.text, 'html.parser')
    genres = soup_data.select("a[href^='/estilos/']") 
    href_genres = []
    for i in genres:
        href = href = i['href'].split('/')[-2]
        #print(href)
        href_genres.append(href)

    n = len(href_genres)
    print(f'All {n} genres found!')

    return(href_genres)

def find_artists_from_genre(genre):
    #genre must be in a specific format to find the right url
    with sync_playwright() as p:
        browser =  p.chromium.launch(headless=invisible_browser)
        page =  browser.new_page()
        dibra_time(4)
        page.goto(f"https://www.letras.mus.br/estilos/{genre}/artistas.html")

        page.locator('a:has-text("Ver todos os artistas")').click()
        time.sleep(3)
        ul_artists =  page.locator('ul[class="cnt-list cnt-list--col3"]')
        print(ul_artists)

        artists =  ul_artists.locator('a')
        n_artists =  artists.count()

        print(f"{n_artists} artists are found.")   

        href_artists = []
        for i in range(n_artists):
            href =  artists.nth(i).get_attribute('href')
            #print(href)
            href_artists.append(href)

        print(f'{genre} finished!')

        browser.close()

        return(href_artists)
    
genres = find_genres()

local_artists = 'E:/coding/github/webscraping_letras/data/raw/artists'
local_songs = 'E:/coding/github/webscraping_letras/data/raw/songs'

# for genre in genres:
#     artists = find_artists_from_genre(genre)
#     sl.save_artists_from_genre(genre,artists,local_artists)