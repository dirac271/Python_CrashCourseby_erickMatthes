#Analisador sintatctico primera parte
question = input("Tell me a number and i'll tell u if it's multiple of 10 or not\n")
question = int(question)
if question % 10 == 0:
    print("Your number it's multiple of 10")
else:
    print("Your number isn't multiple of 10")