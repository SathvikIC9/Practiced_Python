class Employee():
    name = input("Enter Employee name : ")
    age = int(input("Enter Employee age : "))
    experience= int(input("Enter Employee experience : "))
    def details(self):
        print(f"Employee name is : {self.name} \n Employee age is : {self.age} \n Employee experience is : {self.experience}")


class salary(Employee):
    Mi = int(input("Enter monthly income: "))
    
    def income(self):
        print(f"The monthly income is : {self.Mi}")

class increment(salary):
    def increment(self):
        if self.experience>=5:
            self.salary = self.Mi*(5/100)+self.Mi
            print(f"The salary after increment is : {self.salary}")
        elif self.experience >=3:
            self.salary = self.Mi*(3/100)+self.Mi
            print(f"The salary after increment is : {self.salary}")
        else:
            print("No increment")

a = increment()
a.increment()