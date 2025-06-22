'''Write a function count_char(text, char) that counts how many times char appears in text and returns a dictionary like:
{'char': 'e', 'count': 5}'''

text = "Hello world!"
split = text.split()
def count_chars(split):
    char_dict = {}
    for char in split:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    print(char_dict)

count_chars(text)
 


# print(split)