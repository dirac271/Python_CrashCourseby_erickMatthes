
from random import choice
items = [1,2,3,4,5,6,7,8,9,0,'d','s','v','h','q']
winner_list = []
random_ticket = []

def make_random_list():
        ListToRandom = []  
        while len(ListToRandom) < 4:
            ListToRandom.append(choice(items))
        return ListToRandom
winner_list = make_random_list()

attempts = 0
flag = True

print(winner_list)

while True:
      attempts += 1
      random_ticket = make_random_list()
      if winner_list == random_ticket:
            break
print(f"Congratulations! it only took {attempts} attempts!")        