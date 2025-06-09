with open("log.txt","r") as f:
    content = f.read()
with open("copy.txt",'w') as f1:
    f1.write(content)