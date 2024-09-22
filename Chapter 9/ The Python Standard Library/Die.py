from random import randint
class Die:
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        random_sides = randint(1,self.sides)
        return random_sides

dieToTest = Die()

for die in range(10):
    print(dieToTest.roll_die())
print("\n")
tenToTest = Die(10)
twentyToTest = Die(20)
print("\n")
for die in range(10):
    print(tenToTest.roll_die())
print("\n")
for die in range(10):
    print(twentyToTest.roll_die())




