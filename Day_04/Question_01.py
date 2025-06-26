s1 = input("Enter a value: ")
s2 = input("Enter a value: ")
def is_anagram(s1,s2):
    if sorted(s1.lower()) == sorted(s2.lower()):
        print(True)
    else: 
        print(False)
    
is_anagram(s1,s2)
        