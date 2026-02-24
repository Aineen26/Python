class Employee:
    emp_count = 0
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
        Employee.emp_count = Employee.emp_count+1
        self.emp_id = Employee.emp_count
    def display_info(self):
        print(f"Employee_ID: {self.emp_id}")
        print(f"Employee Name:{self.name}")
        print(f"Position:{self.position}")
        print(f"Salary:{self.salary}")
    def get_raise(self,amount):
        self.salary += amount
        print(f"{self.name} got a raise !! New salary is {self.salary}")

emp1 = Employee("Olivia Perkins0","Writer",50000)
emp2 = Employee("Alexander","CEO",600000)
emp3 = Employee("Clara","Assistant Manager",30000)

emp1.display_info()
emp2.display_info()
emp3.display_info()

print(f"Total No. Employee : {Employee.emp_count}")

emp1.get_raise(5000)
emp2.get_raise(80000)

print("Updated data:")

emp1.display_info()
emp2.display_info()