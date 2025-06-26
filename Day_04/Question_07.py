
number = [1, 2, 2, 3, 1, 1]
def freq_dict():
    dictt = {}
    for num in number:
        if num in dictt:
            dictt[num]+=1 
        else:
            dictt[num] = 1
    return dictt

print(freq_dict())
