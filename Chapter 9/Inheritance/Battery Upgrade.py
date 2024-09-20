class Battery:
    def __init__(self, battery_size=50):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 65:
            return 300  # Range for 65 kWh battery
        return 200  # Range for 50 kWh battery

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65


class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def get_range(self):
        return self.battery.get_range()

# Creating an instance of ElectricCar with the default battery size
my_electric_car = ElectricCar('Tesla', 'Model S', 2022)

# Checking the range before upgrading the battery
print(f"Range before upgrade: {my_electric_car.get_range()} miles")

# Upgrading the battery
my_electric_car.battery.upgrade_battery()

# Checking the range after upgrading the battery
print(f"Range after upgrade: {my_electric_car.get_range()} miles")
