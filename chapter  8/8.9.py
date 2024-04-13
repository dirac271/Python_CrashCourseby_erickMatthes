#exercise 8.10
messages = ['Hi how about you','i dont care what u say','do u remember my phyisics']
def show_messages(mensajes):
    for msg in mensajes:
        print(f"The message is: {msg.title()}")
show_messages(messages)

sent_messages = []
def send_messages(menssajes):
    show_messages(menssajes)
    while menssajes:
        current_message = menssajes.pop()
        sent_messages.append(current_message)
send_messages(messages)
print(sent_messages)
print(messages)