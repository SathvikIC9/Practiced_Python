class animals():
    pass


class pets(animals):
    pass
class dog(pets):
    @staticmethod
    def bark():
        print("Woof")



a = dog()
a.bark()
