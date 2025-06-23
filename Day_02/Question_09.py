# Write a function uppercase_values(d) that returns a dictionary where all string values are converted to uppercase.

d = {
    'a': 'hello',
    'b': 'world',

}
def uppercase_values(d):
    return {k: v.upper() for k, v in d.items()}



uppercase_values(d)