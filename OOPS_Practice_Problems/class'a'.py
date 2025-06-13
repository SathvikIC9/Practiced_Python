class idk:
    a = input('Enter the original number: ')  

    def selfcall(self): 
        print(f'The original attribute is {idk.a}')

obj = idk()             
obj.selfcall()          

obj.a = input('Enter the new number: ')  
print(f'The new attribute is {obj.a}')
