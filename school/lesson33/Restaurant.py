class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name)
        print("The restaurant's cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is open.")

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self,additional_served):
        self.number_served += additional_served

restaurant = Restaurant('KFC', 'fast food')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 200
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1000)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(500)
print("Number served: " + str(restaurant.number_served))
