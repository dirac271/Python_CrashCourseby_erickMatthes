#exercise 8.12
def list_sandwich(*items):
    num_elements = len(items)
    if num_elements == 1:
        print(f"the sandwich's item is {items}")
    else:
        print(f"the sandwich's items are {items}")
list_sandwich('chicken')
list_sandwich('tomato','brocoli','chesse')
list_sandwich('drugs','watter')
