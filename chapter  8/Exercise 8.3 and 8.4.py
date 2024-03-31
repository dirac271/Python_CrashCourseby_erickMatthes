#Exercise 8.3 t shirt
def make_shirt(size_shirt,message_shirt):
    print(f"The shirt of size {size_shirt} and with the message '{message_shirt}' is made!")
make_shirt('s',"I'm enrico fermi")
make_shirt(size_shirt='xl',message_shirt='Von Neumann')
#Exercise 8.4
def make_shirt(message_shirt = 'I love Python',size_shirt = 'Large'):
    print(f"The shirt of size {size_shirt} and with the message '{message_shirt}' is made!")
#large and medium shirt, and last message
make_shirt()
make_shirt(size_shirt='medium')
make_shirt(message_shirt='de broglie was a good phycisist')