#Project 3
class RetailItem:
	def __init__(self, description, UII, price):
		self.description = description
		self.Units_in_Inventory = UII
		self.price = price

	def Get_Info(self):
		print("Item Description: " + self.description)
		print("Units in Inventory: " + self.Units_in_Inventory)
		print("Price: $" + self.price)


Item1 = RetailItem("Jacket", "12", "59.95\n")

Item2 = RetailItem("Designer Jeans", "40", "34.95\n")

Item3 = RetailItem("Shirt", "20", "24.95")

Item1.Get_Info()
Item2.Get_Info()
Item3.Get_Info()
