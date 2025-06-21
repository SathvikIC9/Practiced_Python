# Write a function key_exists(d, key) that returns True if the key is in the dictionary, else False.
intents= {
    1:"hello",
    2:"hi",
    3:"bye"
}
a = int(input("Enter the value: "))
b = input("Enter a value: ")
def get_key(intents , keys, values):
    if keys in intents:
        print(True)
    elif values in intents:
        print("Also " ,True)
    else:
        print(False)

    

get_key(intents , keys=(a) ,values=(b) )