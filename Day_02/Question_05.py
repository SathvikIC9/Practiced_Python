# Write a function reverse_dict(d) that returns a new dictionary with keys and values flipped:
# {'a': 1, 'b': 2} ➝ {1: 'a', 2: 'b'}

my_dict ={
    'a': 1,'b':2
}

# print(my_dict[1])
def reverse_dict(d):
    return {v: k for k, v in d.items()}
        

reverse_dict(my_dict)
print(reverse_dict(my_dict))  