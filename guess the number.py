import random 
a = (random.randint(1,10))
wrongs = 0
print("Hello what's your name?")
name = input()
print("Okay"+name+"I am guessing a number between 1 and 10.")
while wrongs < 3:
    answer = int(input())
    if answer == a:
        print("Your answer is true.")
        break
    elif answer < a:
        print("Your answer is low.")
    elif answer > a:
        print("Your answer is high")
    wrongs +=1
print("Game over.")
