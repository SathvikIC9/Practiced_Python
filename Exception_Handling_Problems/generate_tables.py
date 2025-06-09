import os

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    
    os.makedirs("tables", exist_ok=True)
    
    try:
        with open(f"tables/table_{n}.txt", "w") as f:
            f.write(table)
    except IOError as e:
        print(f"Error writing file for table {n}: {e}")

for i in range(2, 21):
    generateTable(i)
