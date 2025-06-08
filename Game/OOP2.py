class Details:
    def __init__(self,animal,group):
        self.animal=animal
        self.group=group
        print(f"The animal {self.animal} belongs to {self.group} group")


animal=str(input("Enter animal name: "))
group= str(input("Enter group : "))
a = Details(animal,group)
