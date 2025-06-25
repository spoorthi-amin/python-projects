num1=float(input("enter first number: "))
num2=float(input("enter second number: "))
operator=input("choose operator (+, -, *, /);")
if operator == "+":
    print("Result:",num1+num2)
elif operator == "-":
    print("Result:",num1-num2)
elif operator=="*":
    print("Result:",num1*num2)
elif operator=="/":
    if num2 != 0:
        print("Result:",num1/num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please choose from +, -, *, /.")