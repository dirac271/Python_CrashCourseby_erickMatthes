from pathlib import Path

name = input("What's your name\n")

path = Path('guest.txt')
path.write_text(name)