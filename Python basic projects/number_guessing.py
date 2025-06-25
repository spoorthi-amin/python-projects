
import random

print("Welcome to the Number Guessing Game!")
secret_num =random.randint(1,10)


while True:
    guess=int(input("Enter a number between 1 and 10 :   "))
    if guess==secret_num:
        print("Smart Guess!! You are LUckkiest!")
        break
    else:
        print("Better Try next time!! the number was" ,secret_num)