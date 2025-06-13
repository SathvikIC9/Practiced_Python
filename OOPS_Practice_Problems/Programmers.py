# create a class programmer for storing info about few prigrammers working at microsoft

a = input("Enter Your Name: ")
b = int(input("Enter Your Salary: "))
c = int(input("Enter Your Age: "))  


class Programmer():
    Employee = a 
    Salary = b 
    Age = c 
    def __init__(self,Employee,Salary,Age):
        self.Employee= Employee
        self.Salary= Salary
        self.Age= Age


    def getInfo(self):
        print(f"Hi {self.Employee}. Your salary is {self.Salary} while your age is {self.Age}")
Programmer1= Programmer(a,b,c)
Programmer1.getInfo()
