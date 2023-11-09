#6-6. Polling:
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
poll = {
 'jen',
 'sarah',
 'edward',
 'phil',
 'josue',
 'ozziel',
 'alejandro',
 }
for name in poll:
    if(name in favorite_languages.keys()):
        print(f"Thankful for responding the poll {name}!")
    else:
        print(f"You should take the poll {name}")

