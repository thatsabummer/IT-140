# Author: Caleb Smith
# Date: 10.20.2023

# Lab 8.9

# Complete the Car class by creating an attribute purchase_price (type int) and the method print_info()
# that outputs the car's information.

# Car value (classes)

class Car:
    def __init__(self):
        self.model_year = 0
      
        # Declare purchase_price attribute
      
        self.purchase_price = 0
        self.current_value = 0

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
      
        # Car depreciation formula
      
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)

    # Define print_info() method to output model_year, purchase_price, and current_value
  
    def print_info(self):
        print("Car's information:")
        print(f'   Model year: {self.model_year}')
        print(f'   Purchase price: {self.purchase_price}')
        print(f'   Current value: {self.current_value}')


if __name__ == "__main__":
    year = int(input())
    price = int(input())
    current_year = int(input())

    my_car = Car()
    my_car.model_year = year
    my_car.purchase_price = price
    my_car.calc_current_value(current_year)
    my_car.print_info()