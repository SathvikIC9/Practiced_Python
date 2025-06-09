with open("erase.txt") as f:
    data =f.read()
    new_data = ""
with open("erase.txt", "w") as f:
    f.write(new_data)