class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"\nThe restaurant {self.restaurant_name} has cuisine {self.cuisine_type}")
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open!")
    def set_number_served(self,numberToSet):
        self.number_served = numberToSet
    def increment_number_served(self,numberToSet):
        self.number_served += numberToSet
restaurant = Restaurant('macdonalds',"extremly ass")
print(f"Number of customers served: {restaurant.number_served}")
restaurant.number_served = 40
print(f"Number of customers served: {restaurant.number_served}")
restaurant.set_number_served(30)
print(f"Number of customers served: {restaurant.number_served}")
restaurant.increment_number_served(304)
print(f"Number of customers served: {restaurant.number_served}")


