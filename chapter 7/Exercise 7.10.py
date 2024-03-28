responses = {}
polling_active = True
while polling_active:
    name = input("What's your name?\n")
    response = input("If you could visit one place in the world, where would you go?\n")
    responses[name] = response

    repeat = input('Would u like to let another person respond this poll?(yes/no)\n\t')
    if repeat == 'no':
        polling_active = False
print("The results of the places poll")
for name,response in responses.items():
    print(name,"They would like to visit", response)    


