secret=5
for attempt in range(3):
    guess = int(input("Guess the secret number (between 1 and 10): "))
    if guess==secret:
        print("Congratulations! You guessed the secret number!")
        break
    else:
        print("Wrong guess. Try again.")