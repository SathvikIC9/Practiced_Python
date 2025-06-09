try:
    with(
        open('text1.txt') as f1,
        open('text2.txt') as f2,
        open('text3.txt') as f3
    ):
        text1 = f1.read()
        text2= f2.read()
        text3= f3.read()
        if 'Harry' in f1:
            print("Yes Harry is present in text1 ")
        elif 'Harry' in f2:
            print("Harry is there in Text2 ")
        elif 'Harry' in f3:
            print("Yes Harry is present in Text2")
        else:
            print("Harry not found in")

except FileNotFoundError:
    print("The File was not found")

        