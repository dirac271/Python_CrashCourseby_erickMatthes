from pathlib import Path
path = Path('learning_python.txt')
contents = path.read_text().replace('Python','C')

print(contents)

lines = contents.splitlines()

for line in lines:
    line = line.replace('sex','EPICO')
    print("\t\n" + line)

