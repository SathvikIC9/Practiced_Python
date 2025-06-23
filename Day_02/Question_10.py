import string
sentence = "Hello , Hello how are you?"
sentence = sentence.translate(str.maketrans('', '', string.punctuation))
split = sentence.split()
def word_freq(split):
    freq = {}
    for word in split:
        if word in freq:
            freq[word] +=1
        else:
            freq[word]= 1
    print(freq)

word_freq(split)
