#Project 1 (class only)
class Pet:
	def __init__(self, name, animal_type, age):
		self.set_name(name)
		self.set_animal_type(animal_type)
		self.set_age(age)

	def set_name(self, name):
		self.__name = name

	def set_animal_type(self, animal_type):
		self.__animal_type = animal_type

	def set_age(self, age):
		self.__age = age

	def get_name(self):
		return self.__name

	def get_animal_type(self):
		return self.__animal_type

	def get_age(self):
		return self.__age

