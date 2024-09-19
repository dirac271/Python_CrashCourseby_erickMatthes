import random


class User:
    def __init__(self,first_name,last_name,pin_user,english_or_spanish):
        self.first_name = first_name
        self.last_name = last_name
        self.pin_user = pin_user
        self.english_or_spanish = english_or_spanish

    def describe_user(self):
        print(f"The user {self.first_name} {self.last_name} with {self.pin_user} pin prefered {self.english_or_spanish}")
    
    def greet_user(self):
        print(f"What's up fucking {self.last_name}!")

random_users = [
    User("Cactus", "McNugget", random.randint(1000, 9999), "English"),
    User("Taco", "Frito", random.randint(1000, 9999), "Spanish"),
    User("Pickle", "Juice", random.randint(1000, 9999), "English"),
    User("Gato", "Loco", random.randint(1000, 9999), "Spanish"),
    User("Captain", "N", random.randint(1000, 9999), "English"),
]
for user in random_users:
    user.describe_user()
    user.greet_user()
    print()
