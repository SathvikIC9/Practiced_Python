def  rev_word(s):
    if s==s[::-1]:
        print("Its a plaindrome")
    else:
        print("Its not a palindrome")

s = input("Enter a word: ")
rev_word(s)
