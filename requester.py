import requests
import json
from halo import *


def push_track():
    count = 0
    with open("./data/tracks.json", "r") as j:
        tracks = json.load(j)
        for track in tracks:
            try:
                requests.post('http://localhost:5500/api/addTrack', track)
                count += 1
            except:
                print('smt went wrong check express log')
    print("\n" + str(count) + ' tracks has been added')


def push_album():
    count = 0
    with open("./data/albums.json", "r") as j:
        albums = json.load(j)
        for album in albums:
            try:
                res = requests.post('http://localhost:5500/api/addAlbum', album)
                print(res.json())
                count += 1
            except:
                print('smt went wrong check express log')
    print("\n" + str(count) + ' albums has been added')


def push_artist():
    count = 0
    with open("./data/artists.json", "r") as j:
        artists = json.load(j)
        for artist in artists:
            try:
                requests.post('http://localhost:5500/api/addArtist', artist)
                count += 1
            except:
                print('smt went wrong check express log')
    print("\n" + str(count) + ' artists has been added')


spinner = Halo(text='Adding Tracks', spinner='dots')
spinner.start()
push_track()
spinner.stop()

spinner = Halo(text='Adding Albums', spinner='dots')
spinner.start()
push_album()
spinner.stop()

spinner = Halo(text='Adding Artists', spinner='dots')
spinner.start()
push_artist()
spinner.stop()