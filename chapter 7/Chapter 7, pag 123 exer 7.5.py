text1 = "Ok i'll tell you how much you have to pay per ticket so\n"
text1 += "Tell me how old are u and i'll tell you how much you have to pay\n"
text1 += "type -1 to exit\n"
age = 0
while age != -1: 
    print(text1)
    age = int(input())        
    if age > 0 and age < 3:
        print("You'll pass free!\n")
    elif age > 3 and age < 12:
        print("You'll pay 10$ for the ticket!\n")  
    elif age > 12:
        print("You'll pay 15$ for the ticket!\n")