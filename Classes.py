class Track:

    def __init__(self, title, artist, album, img_url, lyrics):
        self.title = title
        self.artist = artist
        self.album = album
        self.img_url = img_url
        self.lyrics = lyrics


class Album:

    def __init__(self, title, artist, tracks, img_url, date_of_publication):
        self.title = title
        self.artist = artist
        self.tracks = tracks
        self.img_url = img_url
        self.date_of_publication = date_of_publication


class Artist:

    def __init__(self, full_name, tracks, albums, img_url):
        self.full_name = full_name
        self.tracks = tracks
        self.albums = albums
        self.img_url = img_url





