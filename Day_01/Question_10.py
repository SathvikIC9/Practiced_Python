# Write a function char_frequency(text) that returns a dictionary where keys are characters and values are how many times they appe
sentence = "Helloo there nice to meet you"
def char_frequency(sentence):
    dict_freq= {}
    for char in sentence:
        if char in dict_freq:
            dict_freq[char] +=1
        else:
            dict_freq[char] = 1
    print(dict_freq)
    
char_frequency(sentence)