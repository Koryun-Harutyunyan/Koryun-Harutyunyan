import random 
a = (random.randint(1,10))
wrongs = 0
print("Hello what's your name?")
name = input()
print("Okay "+name+" I am guessing a number between 1 and 10.")
def my_function():
    if answer < a:
        print("Your answer is low.")
    if answer > a:
        print("Your answer is high")
    
while wrongs < 3:
    answer = int(input())
    if answer == a:
        print("Your answer is true.")
        break
    my_function()
    wrongs += 1
print("Game over.")
