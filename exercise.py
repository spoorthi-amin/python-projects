import time

# t=time.strftime('%H: %M :%S')

hour=int(time.strftime('%H'))
print(hour)
# print(hour)
# hour=int(input("enter hour" ))
# 
if hour>=0 and hour<12:
    print("Good Morning Sir")
elif hour>=12 and hour<17:
    print("Good Afternoon sir")
elif hour>=17 and hour<0:
    print("Good night sir")
