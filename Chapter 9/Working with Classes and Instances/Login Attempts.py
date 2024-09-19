import random


class User:
    def __init__(self,first_name,last_name,pin_user,english_or_spanish):
        self.first_name = first_name
        self.last_name = last_name
        self.pin_user = pin_user
        self.english_or_spanish = english_or_spanish
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user {self.first_name} {self.last_name} with {self.pin_user} pin prefered {self.english_or_spanish}")
    
    def greet_user(self):
        print(f"What's up fucking {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

pepeElGrillo = User("caca","malone",123,"english")

pepeElGrillo.increment_login_attempts()
pepeElGrillo.increment_login_attempts()
pepeElGrillo.increment_login_attempts()
pepeElGrillo.increment_login_attempts()
pepeElGrillo.increment_login_attempts()
print(pepeElGrillo.login_attempts)
pepeElGrillo.reset_login_attempts()
print(pepeElGrillo.login_attempts)
