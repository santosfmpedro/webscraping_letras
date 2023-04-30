
import pandas as pd
import os

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
        print(f'{local}/{genre}/{artist} saved!')
