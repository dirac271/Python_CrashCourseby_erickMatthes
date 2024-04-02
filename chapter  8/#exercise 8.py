#exercise 8.7 Album
def make_album(artist_album,title_album,album_songs = None):
    album = {'Artist:':artist_album,'Title':title_album}
    if album_songs:
        album['Album songs'] = album_songs
    return album
# exercise 8.8
print('You can type "q" at any time to quit')
artist_prompt = "What's the artist are you thinking of?\n"
title_prompt = "What's the album are you thinking of?\n"
while True:
    artist = input(artist_prompt)
    if artist == 'q':
        break
    title = input(title_prompt)
    if title == 'q':
        break
    album_print = make_album(artist,title)
    print(album_print)
print('That was all,thankful')
        


