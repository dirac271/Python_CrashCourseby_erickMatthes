from pathlib import Path
file = Path('guest_book.txt')

while True:
    name = input("Tell me ur name\n")
    if(name == 'exit'):
        break
    contents = file.read_text()
    contents += name + "\n"
    contents += "CEO OF SEX HAS WRITTEN A NEW LINE BITCHES\n"
    file.write_text(contents)
