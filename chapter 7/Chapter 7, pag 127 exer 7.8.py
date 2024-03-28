sandwich_orders = ["subway PP","Peperoni pai","CHESSE","Vegetables"]
finished_sandwiches = []
prefix = "\nI made your "
while sandwich_orders:
    print(prefix + sandwich_orders[-1])
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
print("\nAll of this sandwiches was made:")
for sandwich in finished_sandwiches:
    print(f"The sandwich {sandwich.title()} was made!")
