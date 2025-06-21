# Write a function get_value(d, key) that returns the value from a dictionary d for the given key.

fruits = {
    'apple': 5,
    'banana': 10,
    'cherry': 15
}
def get_value(fruits,key):
    return fruits.get(key)

print(get_value(fruits,"apple"))