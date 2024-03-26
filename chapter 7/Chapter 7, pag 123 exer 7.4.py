topping = "Tell me your topping to add to the pizza"
topping += "\nIf are ready with ur toppings type 'quit'\n"
message = ''
while message != 'quit':
    message = input(topping)
    if message != 'quit':
        print("Okey we'll add " + message + " to your pizza")