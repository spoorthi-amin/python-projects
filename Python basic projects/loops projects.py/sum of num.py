while True:
    num=int(input("enter a number :   "))
    total=0
    for i in range( 1,num+1):
        total+=i
    print(f"The sum of numbers from 1 to {num} is {total}")