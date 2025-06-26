def duplicate(l):
    duplicate=[]
    for i in set(l):
        if l.count(i) >1:
            duplicate.append(i)
    return duplicate
l = [1, 2, 3, 2, 4, 1] 
print(duplicate(l))  
