number1=int(input("enter the number1 "))
number2=int(input("enter the number2 "))
number3=int(input("enter the number3 "))
if(number1<=number2 and number1<=number3):
    print("number1 is minimum")
elif (number2<=number3 and number2<=number1):
    print("number2 is minimum")
else:
    print("number3 is minimum")
 