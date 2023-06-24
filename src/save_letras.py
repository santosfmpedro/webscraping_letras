
import pandas as pd
import os
import glob

def read_genres(folder):
    genres_artists_files = glob.glob(f"{folder}/*")
    return(genres_artists_files)

def read_any(folder):
    any = glob.glob(f"{folder}/*")
    return(any)

def read_artists(genre):
    artists = pd.read_csv(genre, header=None)
    artists = artists.rename(columns={0: 'artists'})
    return(artists)

def read_songs(artist):
    songs = pd.read_csv(artist, header=None)
    songs = songs.rename(columns={0: 'songs'})
    return(songs)

def create_dir(name,local):
    path = os.path.join(local, name)

    try:
        os.mkdir(path)
        print("Directory '% s' created" % name)
    
    except:
        print("Maybe directory already exists!")

def save_artists_from_genre(genre,list_artists,local):
    with open(f'{local}/{genre}.txt','w+') as fp:
        for item in list_artists:
            # write each item on a new line
            fp.write("%s\n" % item)
        print(f'{local}/{genre} saved!')


def save_songs_from_artist(genre,artist,list_musics,local):
    with open(f'{local}/{genre}___{artist}.txt','w+') as fp:
        for item in list_musics:
            # write each item on a new line
            fp.write("%s\n" % item)
        print(f'{local}/{genre}___{artist} saved!')

def save_lyric_from_a_song(genre,artist,song,lyric_list,local):
    with open(f'{local}/{genre}___{artist}___{song}.txt','w+') as fp:
        for item in lyric_list:
            # write each item on a new line
            fp.write("%s\n" % item)
        print(f'{local}/{genre}___{artist}___{song} saved!')