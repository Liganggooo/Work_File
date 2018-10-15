class Restaurant():		
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describle_restaurant(self):
		print("The rastaurant name is: " + self.restaurant_name.title())
		print("we have lost of cuisine type: " + self.cuisine_type)
	def open_restaurant(self):
		print("The restaurant is open")


restaurant = Restaurant('the mean queen', 'pizza')

print("my restaurant name is " + restaurant.restaurant_name.title())
restaurant.describle_restaurant()
restaurant.open_restaurant()
