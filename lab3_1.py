class Employee:
    def __init__(self,name,date_of_join,designation,salary):
        self.name=name
        self.date_of_join=date_of_join
        self.designation=designation
        self.salary=salary
    def display_details(self):
        print("employee name:  ",self.name)
        print("date of join: ",self.date_of_join) 
        print("designation:  ",self.designation)
        print("salary:  ",self.salary)

emp=Employee("Tanvi Mehta","03-07-2024","software engineer",80000)
emp.display_details()
    
