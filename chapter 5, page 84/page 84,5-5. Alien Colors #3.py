#5-5. Alien Colors #3: first version
alien_color = 'green'
if alien_color == 'green':
    print("you have earned 5 points")
elif alien_color == 'yellow':
    print("you have earned 10 points")
elif alien_color == 'red':
    print("you have earned 15 points")
#2th version
points = 5
if points == 5:
    alien_color = 'green'
elif points == 10:
    alien_color == 'yellow'
elif points == 15:
    alien_color == 'red'
print(f"you have earned {points} points")
#third version
aliens_color = ['red','green','yellow']
for alien in aliens_color:
    if alien == 'red':
        print("you haven earned 15 points")
    elif alien == 'yellow':
        print("you haven earned 10 points")  
    elif alien == 'green':
        print("you haven earned 5 points")  