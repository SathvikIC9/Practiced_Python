# "The sky is blue and the sea is blue" ➝ "blue" most repeated word

# word = s.count()
# print(s)
def most_repeated(s):
    s = l.split()
    return max(set(s), key = s.count)

l = "The sky is blue and the sea is blue" 
print(most_repeated(l))
