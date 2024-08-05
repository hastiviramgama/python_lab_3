class Company:
    def __init__(self,name,city,mobile_no):
        self.name=name
        self.city=city
        self.mobile_no=mobile_no
    def display_company(self):
        print("name:  ",self.name)
        print("city: ",self.city)
        print("mobile_no:  ",self.mobile_no)

class employee(Company):   #create class employee 
    def __init__(self,emp_name,designation,salry,name,city,mobile_no):
        self.emp_name=emp_name
        self.designation=designation
        self.salary=salry
        super().__init__(name,city,mobile_no)
    def display_employee(self):
        print("employee name:  ",self.emp_name)
        print("designation: ",self.designation)
        print("salary:  ",self.salary)
emp=employee("Harsil Mehata","software engineer",90000,"arohi","rajkot",8589585454)
emp.display_employee()