class Details:
    name = str(input("Enter your name: "))
    age =int(input("Enter your age: "))

    def me(self):
       
        print(f"Hi my name is {self.name} and my age is {self.age}")

a = Details()
a.me()

