

import requests
from bs4 import BeautifulSoup
import pandas as pd
import glob
import sys
 
sys.path.insert(0, 'E:/coding/github/webscraping_letras/src')

import save_letras as sl
import site_genre_playwright as lp

local_artists = 'E:/coding/github/webscraping_letras/data/raw/artists'
local_songs = 'E:/coding/github/webscraping_letras/data/raw/songs'
local_lyrics = 'E:/coding/github/webscraping_letras/data/raw/lyrics'


def find_all_lyrics_from_all_genres(local_artists,local_songs,local_lyrics):
    genres = sl.read_genres(local_artists)
    for i in range(len(genres)):
        
        artists = sl.read_artists(genres[i])
        genre_clean = genres[i]

        for j in range(len(artists)):
            artist = artists['artists'][j].replace('/','')
            genre = genres[i].split('\\')[-1].replace('.txt','')
            try:
                songs = sl.read_songs(f'{local_songs}/{genre}___{artist}.txt')
            except:
                print('Error reading song')

            for song in songs['songs']:
                print(song)
                try:
                    output = lp.find_lyric_from_song(song)
                except:
                    print('Error finding lyric from song')
                song_clean = song.replace('/','_')
                sl.save_lyric_from_a_song(genre,artist,song_clean,output,local_lyrics)

find_all_lyrics_from_all_genres(local_artists,local_songs,local_lyrics)