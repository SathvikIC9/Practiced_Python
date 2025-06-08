class Employee():
    def __init__(self, name, age, salary):
     self.name = name
     self.age = age
     self.salary = salary
     print(f"The Name is {self.name} and age is {self.age} with salary {self.salary}")


name = str(input("Enter Name: "))
age = str(input("Enter age: "))
salary = str(input("Enter salary: "))

b = Employee(name, age , salary )