try:
    word = 'donkey'
    with open("My_file.txt",'r') as f:
        content = f.read()
       
        word_new = word.replace(word,'#####')
    with open("My_file.txt",'w') as f:
        f.write(word_new)
except ValueError:
    print("Word not found")