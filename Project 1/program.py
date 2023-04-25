#Project 1 (program only)
import class1

def main():

	name = (input('enter the name '))
	animal_type = (input('enter the animal type '))
	age = (input('enter the age '))

	pet1 = class1.Pet(name, animal_type, age)

	v1 = pet1.get_name()
	v2 = pet1.get_animal_type()
	v3 = pet1.get_age()

	print(v1 , v2, v3)
main()