from selenium import webdriver
from halo import Halo
import json
from util import *
from Classes import *

count = 0


def create_album_obj(albums, artist_name, img_urls, tracks):
    n = len(albums)
    for i in range(n):
        aa = Album(albums[i], artist_name, tracks[i].split("\n"), img_urls[i], None)
        album_obj.append(aa)


def create_artist_obj(full_name, tracks, albums, img_url):
    aa = Artist(full_name, tracks, albums, img_url[0])
    artist_obj.append(aa)


def create_track_obj(obj):
    t = obj.tracks
    a = obj.artist
    i = obj.img_url
    for j in t:
        comp = extract_link(j, 2)
        for link in track_links:
            if comp in link:
                if get_lyrics(link) is not None:
                    track_obj.append(Track(j, a, obj.title, i, get_lyrics(link)))


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


def extract_link(string, n):
    start1 = string.find('(') + 1
    end1 = find_nth(string, ')', n)
    mystr = string[start1:end1]
    return mystr.replace(" ", "_")


def find_album_from_track(track, album_obj):
    track = track[track.find('(') + 1: find_nth(track,')', 2)]
    for o in album_obj:
        if track in o.tracks:
            return o


path = "/home/besufikad/Documents/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://wikimezmur.org/am/Gospel_Singers")
# p = driver.find_elements(By.XPATH, '//table/tbody')
p = driver.find_elements_by_class_name('mw-parser-output')

artist_obj = []
album_obj = []
track_obj = []
artists = []
albums = []
tracks = []
img_urls = []
artist_links = []
track_links = []
years = []

spinner = Halo(text='Loading', spinner='dots')

for elements in p:
    spinner.start()
    artists = elements.text.split("\n")

spinner.stop()
artists = artists[3:]

for a in artists:
    try:
        s = a[a.index('(') + 1: a.index(')')]
        l = s.split()
        if len(l) == 1:
            pass
        else:
            artist_links.append('https://wikimezmur.org/am/' + l[0] + '_' + l[1])
            driver.get('https://wikimezmur.org/am/' + l[0] + '_' + l[1])
            search = driver.find_elements_by_class_name('toctext')
            imgs = driver.find_elements_by_tag_name('img')
            dls = driver.find_elements_by_tag_name('dl')
            for e in search:
                albums.append(e.text)
            for t in imgs:
                img_urls.append(t.get_attribute('src'))
            for d in dls:
                tracks.append(d.text)
                alink = d.find_elements_by_css_selector("*")
                for al in alink:
                    if str(al.get_attribute('href')).count('/') < 7 and al.get_attribute('href') is not None:
                        track_links.append(str(al.get_attribute('href')))

            create_album_obj(albums, a, img_urls, tracks)
            create_artist_obj(s, tracks, albums, img_urls)
            albums = []
            tracks = []
    except:
        pass


arr = []
for o in album_obj:
    if count == 100:
        break
    else:
        create_track_obj(o)
        arr.append({
            'title': o.title,
            'artist': o.artist,
            'tracks': o.tracks,
            'img_url': o.img_url,
            'date_of_release': " "
        })
        count += 1

with open("./data/albums.json", "w", encoding = 'utf8') as j:
    json.dump(arr, j, ensure_ascii=False, indent=4)

arr = []

for a in artist_obj:
    arr.append({
            'full_name': a.full_name,
            'albums': a.albums,
            'tracks': a.tracks,
            'img_url': a.img_url,
    })

with open("./data/artists.json", "w", encoding = 'utf8') as j:
    json.dump(arr, j, ensure_ascii=False, indent=4)


arr = []

for track in track_obj:
    arr.append({
            'title': track.title,
            'album': track.album,
            'artist': track.artist,
            'img_url': track.img_url,
            'lyrics': track.lyrics
    })

with open("./data/tracks.json", "w", encoding='utf8') as j:
    json.dump(arr,j , ensure_ascii=False, indent=4)
driver.quit()