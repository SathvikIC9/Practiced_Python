# Write a function merge_dicts(d1, d2) that merges both dictionaries. If a key exists in both, use the value from d2.
d1 ={ 1: 'a', 2: 'b', 3: 'c'}
d2 = { 3: 'd', 4: 'e', 5: 'f'}
def merge_dicts(d1, d2):
            for key in d2.keys():
                d1[key] = d2[key]
            print(d1)


merge_dicts(d1, d2)
