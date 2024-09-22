from random import choice
items = [1,2,3,4,5,6,7,8,9,0,'d','s','v','h','q']
class GenerateNumber:
    def __init__(self,list = []):
        self.list = list
    
    def randomList(self,listToRandom):
        self.list = listToRandom
        while len(self.list) < 4:
            listToRandom.append(choice(items))
        return self.list
    
