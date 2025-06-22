a = {
    "Harry":100,"Shub":100
}
# print(a["Harry"])
def find_max_value(a):
    print(max(a, key=a.get))  # Returns the key with the highest value

find_max_value(a)
