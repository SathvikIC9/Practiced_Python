# Write a function get_keys_values(d) that returns a list of keys and a list of values separately.

a = {
    1: 'harry', 2: 'IC', 3: 'shub'
}

def get_keys_values(a):
    b = list(a.keys())
    c = list(a.values())
    print(b)
    print(c)


get_keys_values(a)