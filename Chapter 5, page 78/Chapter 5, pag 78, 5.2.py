#Ex2
#Minifacebook page

user1 = 'Alejandro'
user2 = 'De Broglie'
user3 = 'Szilard'
user4 = 'Fourier'
user5 = 'Pauli'
user6 = 'Schrodinger'
generalage = 20
user1age = 19
user2age = 35
user3age = 29
user4age = 38
user5age = 31
user6age = 27


print("The first user wants to name herself 'Alejandro'")
print(user1 == 'Alejandro')

if user2 != 'Alejandro':
    print("You're right, you're not Alejandro, true")

print("You're older than 20y/o?")
print(user1age == 19)

print("And you us2?")
print(user2age > 20)

print("user3 is younger than 20?")
print(user3age < 20)

print("What's is name of user1?")
print(user1.lower())

print("Alejandro and de broglie are older than 20?")
print(user1age >= 20 and user2age >= 20)

print(user3 +" and " + user4 + " one of them are younger than 20?")
print(user3age <= 20 or user4age <= 20)

nobelprize_winnings = [user2,user5,user6]
print("Winners of nobel prizew, are debroglie?")
print(user2 in nobelprize_winnings)

print("And " + user1 + " Won nobel")
print(user2 in nobelprize_winnings)