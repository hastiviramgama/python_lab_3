class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee:
    def __init__(self, emp_id, designation):
        self.emp_id = emp_id
        self.designation = designation
    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)

class StaffMember(Person, Employee):
    def __init__(self, name, age, emp_id, designation):
        Person.__init__(self, name, age) 
        Employee.__init__(self, emp_id, designation) 
    def display_staff(self):
        Person.display_person(self)
        Employee.display_employee(self) 
        
staff = StaffMember("Aacharya Gupta", 30, "343c", "Software Engineer")
staff.display_staff()
