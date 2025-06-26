balance=7000

for i in range(3):
    amt=int(input("Enter the amount to withdraw: "))
    if amt< balance:
        balance -= amt
        print(f"Transaction successful! Your new balance is: {balance}")
        break
    else:
        print("Insufficient balance. Please try again.")
        print("Thank you for using our ATM service!")

