# if you use some IDE, please install an extension for checking coding style
# otherwise, you can use one of the provided in the below link tools
# https://www.infoworld.com/article/3572276/python-style-5-tools-to-clean-up-your-python-code.html 

import random

# functions need to be defined at the beginning of the script
# please give functions a meaningful name that makes your code easier to understand.
def check_number(memorized_number, guessed_number):
    if memorized_number == guessed_number:
        print("You are right!")
        return True
    if memorized_number < guessed_number:
        print("Your answer is low.")
        return False
    print("Your answer is high")
    return False

def input_user_data():
    print("Hello what's your name?")
    name = input()
    print("Okay "+ name +" I am guessing a number between 1 and 10.") # TODO with %s
    
if __name__ == "__main__":
    memorized_number = (random.randint(1, 10))
    attempts = 0
    input_user_data()
    
    while attempts < 3:
        guessed_number = int(input())
        is_checked = check_number(memorized_number, guessed_number)
        if is_checked:
            break
        attempts += 1
    print("Game over.")
