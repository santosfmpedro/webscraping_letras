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

def find_songs_from_artist(artist):
    dibra_time(1)
    res = requests.get(f'https://www.letras.mus.br/{artist}/')
    soup_data = BeautifulSoup(res.text, 'html.parser')
    songs = soup_data.select("a[class='song-name']")
    if (len(songs) == 0):
        songs = soup_data.select("li[class='cnt-list-row -song']")
        href_songs = []
        for i in songs:
            href = i.find('a').get('href')
            href_songs.append(href)
    else:
        href_songs = []
        for i in songs:
            href = i['href']
            href_songs.append(href)

    print(f'{artist} songs found!')
    return(href_songs)


# artist = artists['artists'][0].replace('/','')
# genre = genres[0].split('\\')[-1].replace('.txt','')

# genres = find_genres()

# local_artists = 'E:/coding/github/webscraping_letras/data/raw/artists'
# local_songs = 'E:/coding/github/webscraping_letras/data/raw/songs'

# for genre in genres:
#     artists = find_artists_from_genre(genre)
#     sl.save_artists_from_genre(genre,artists,local_artists)

def find_lyric_from_song(song):
    res = requests.get(f'https://www.letras.mus.br/{song}')
    soup_data = BeautifulSoup(res.text, 'html.parser')

    header = soup_data.select("div[class='cnt-head cnt-head--l']") 
    all_lyric = soup_data.select("div[class='cnt-letra']") 

    for th in header:
        artist_output = th.find('span').text
        views = th.find("b").text
        name_song = th.find("h1").text
        song = f'Song: {name_song}'
        artist_output = f'Artist: {artist_output}'
        print('10')
        views = f'Views: {views}'
        print(artist_output)

    verses = []

    for i in all_lyric:
        aux = i.find_all("p")
        n = len(aux)
        n_verses = f'Verses: {n}'

        for j in aux:
            verse = j.get_text(strip=True, separator= '\n').splitlines()
            for z in verse:
                verses.append(z)
            verses.append('\n')
    
    output = [song, artist_output,views, n_verses, verses]

    return(output)