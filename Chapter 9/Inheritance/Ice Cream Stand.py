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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def DisplayFlavors(self):
        for flavor in self.flavors:
            print(flavor)    

ice_cream_stand = IceCreamStand("Sweet Treats", "Dessert", ["Vanilla", "Chocolate", "Strawberry", "Mint", "Cookie Dough"])
ice_cream_stand.DisplayFlavors()