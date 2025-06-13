class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,v2):
        return vector(self.x+v2.x,self.y+v2.y,self.z+v2.z)
    def __mul__(self, v2):
        return vector(self.x * v2.x, self.y * v2.y, self.z * v2.z)
    def __str__(self):
        return f"({self.x})x+({self.y})y+({self.z})z"
    def __len__(self):
        return len([self.x,self.y,self.z])
    
v1 = vector(1,2,3)
v2 = vector(1,2,3)
print(v1 + v2)
print(v1*v2)
print(len(v1+v2))
print(len(v1*v2))