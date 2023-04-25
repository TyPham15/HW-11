#Project 2
class Employee:
	def __init__(self, name, id_number, department, job_title):
		self.name = name
		self.id_number = id_number
		self.department = department
		self.job_title = job_title

	def Get_Info(self):
		print("Name: " + self.name)
		print("ID Number: " + self.id_number)
		print("Department: " + self.department)
		print("Job Title: " + self.job_title)


Employee1 = Employee("Susan Meyers", "47899", "Accounting", "Vice President\n")

Employee2 = Employee("Mark Jones", "39119", "IT", "Programmer\n")

Employee3 = Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

Employee1.Get_Info()
Employee2.Get_Info()
Employee3.Get_Info()
