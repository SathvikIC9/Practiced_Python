with open("copy.txt") as f :
    content = f.read()

with open("log.txt") as f1 :
    content1 = f1.read()

if content == content1 :
    print("Yes these are same.")
else:
    print("No these are not same.")
    