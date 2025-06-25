import random 
print("Welcome   to    Rock    Paper    Scissor    Game  ")


symbols=["rock","paper", "scissor"]




User_choice=int(input("Enter your choice ,Type 0 for rock ,1 for paper and 2 for scissor:   "))
if User_choice>=0 and User_choice<=2:
    print("You chose:",symbols[User_choice])

computer_choice=random.randint(0,2)
print("Computer_choice:",symbols[computer_choice])

if User_choice>=3 or User_choice<0:
    print("Invalid choice !!! Enter right choice, Computer Won")
elif User_choice==computer_choice:
    print("Match draw!!")
elif User_choice > computer_choice:
    print("You Win!")
elif User_choice==0 and computer_choice==2:
    print("You Win!")
elif User_choice==2 and computer_choice==0:
    print("Computer Win!")
elif computer_choice>User_choice:
    print("computer win!!")
