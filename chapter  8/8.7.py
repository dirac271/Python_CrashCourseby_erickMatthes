#exercise 8.7 Album
def make_album(artist_album,title_album,album_songs = None):
    album = {'Artist:':artist_album,'Title':title_album}
    if album_songs:
        album['Album songs'] = album_songs
    return album
album_print = make_album('Tainy','DATA')
album_print = make_album('Posty','Stoney',12)
print(album_print)

