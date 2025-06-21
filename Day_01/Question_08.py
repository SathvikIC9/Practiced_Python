# Write a function update_value(d, key, new_value) that updates the value of the given key in the dictionary.

a = {
    1: 'harry', 2: 'IC', 3: 'shub'
}
b =int(input("Enter the key : "))
c =input("Enter the value : ")

def update_key(a,b,c):
    a[b]=c
    print(a)

update_key(a,b,c)
   