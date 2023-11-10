#6-7. People:
Dirac = {'first_name':'Paul','last_name':'Dirac','age':31,'City':'Bristol'}
Oppenheimer = {'first_name':'Robert','last_name':'Oppenheimer','age':19,'City':'New York',}
Neumann = {'first_name':'Jonh','last_name':'Von Neumann','age':'26','City':'Budapest'}
people = [Dirac,Oppenheimer,Neumann]

for person in people:
    print("\nName:", person['first_name'])
    print("Last Name:", person['last_name'])          
    print("Age:", person['age'])
    print("City:", person['City'])