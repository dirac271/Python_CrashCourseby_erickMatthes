class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"\nThe restaurant {self.restaurant_name} has cuisine {self.cuisine_type}")
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open!")


Coban = Restaurant("Comedor pioch","DONJuanas")
CarchaComedores = Restaurant("Pene","Mercado Cantonal")
CarchaPuticlubs = Restaurant("SecsiLeidis","Wakala jajajj")

Coban.describe_restaurant()
CarchaComedores.describe_restaurant()
CarchaPuticlubs.describe_restaurant()
