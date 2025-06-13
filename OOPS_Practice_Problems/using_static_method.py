#  adding a static into this 
a = int(input('Enter a Number: '))

class Calculator:
    def __init__(self, a):
        self.a = a
        self.squareroot = a ** 0.5
        self.square = a ** 2
        self.cube = a ** 3
    @staticmethod
    def greet():
        print('hello')

    def callFn(self):
        print(f'The squareroot of {self.a} is {self.squareroot}.The square is {self.square}.The cube is {self.cube}.')
       

obj = Calculator(a)
obj.callFn()
obj.greet()