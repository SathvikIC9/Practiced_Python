# change th parameter drom self to slf 


a = int(input('Enter a Number: '))

class Calculator:
    def __init__(slf, a):
        slf.a = a
        slf.squareroot = a ** 0.5
        slf.square = a ** 2
        slf.cube = a ** 3

    def callFn(slf):
        print(f'The squareroot of {slf.a} is {slf.squareroot}.The square is {slf.square}.The cube is {slf.cube}.')
       

obj = Calculator(a)
obj.callFn()
