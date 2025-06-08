import random

def game():
    print("You are playing a game : ")
    score = random.randint(1,100)
    #fetch results 
    with open("Highscore.txt") as f:
        highscore = f.read()
        if (highscore!=''):
            highscore = int(highscore)
        else: highscore = 0
       
    print(f"Your score is = {score}")
    if (score > highscore):
        with open("Highscore.txt", 'w') as f:
            f.write(str(score))

    print(f"Your highscore is= {highscore}")    

    return score 

game()