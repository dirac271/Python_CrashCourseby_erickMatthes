#Analisador sintatctico primera parte
question = input("How many people are at the dinner?\n")
question = int(question)
if question > 8:
    print("Y'all will have to wait for a table")
else:
    print("Your table is ready!")