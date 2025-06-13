class vector():
    i = (int(input("Enter i value: ")))
    j = (int(input("Enter j value: ")))
    def two_D_vector(self):
        print(f"The vector lies in 2-D plane who's coodinates are ({self.i},{self.j})")

class three_dim_vectors(vector):
    k = (int(input("Enter k value: ")))
    def three_D_vector(self):
        print(f"The vector lies in 3-D plane who's coordinates are ({self.i},{self.j},{self.k})")

a = vector()
b = three_dim_vectors()

a.two_D_vector()
b.three_D_vector()