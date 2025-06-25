pin="1234"

while True:
    input_pin=input("PIN >>  ")
   
    if input_pin==pin:
            print("PIN Accepted")
            break
    else:
         print("wrong Pin")
