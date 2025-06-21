# Write a function word_count(sentence) that returns a dictionary of word counts from a string.
def word_count(sentence):
    words = sentence.split()
    print(f"The words are: {words}")
    
    word_count_dict = {}
    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict

# Input sentence
sentence = "Hi i am good"

# Call function and store result
b = word_count(sentence)

# Count number of words (keys in dictionary)
a = len(b)
print(f"The number of unique words is: {a}")
print(f"Word counts: {b}")
