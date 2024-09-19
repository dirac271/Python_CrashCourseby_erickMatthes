class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"\nThe restaurant {self.restaurant_name} has cuisine {self.cuisine_type}")
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open!")

FirstInstance = Restaurant('Pizza hut','Italian')
print(FirstInstance.restaurant_name)
print(FirstInstance.cuisine_type)

FirstInstance.describe_restaurant()
FirstInstance.open_restaurant()
