sandwich_orders = ["subway PP","pastrami","pastrami","Peperoni pai","pastrami","CHESSE","Vegetables"]
finished_sandwiches = []
prefix = "\nI made your "
print('Deli has ran out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    print(prefix + sandwich_orders[-1])
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
print("\nAll of this sandwiches was made:")
for sandwich in finished_sandwiches:
    print(f"The sandwich {sandwich.title()} was made!")
