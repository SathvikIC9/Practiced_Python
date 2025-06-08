import random
n = random.randint(1,20)
a = -1
guesses = 0 
while (a !=n):
    a = int(input("Enter your guess :"))
    if(a>n):
        print("Lower number please .")
        guesses += 1 

    elif(a<n):
        print("Higher number please .")
        guesses += 1 

print(f"You have guessed the number {n} in {guesses} guesses")