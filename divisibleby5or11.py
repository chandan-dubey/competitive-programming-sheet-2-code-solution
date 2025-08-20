number=int(input("enter a number"))
if (number%5==0 or number%11==0):
  print(f"{number} is divisible by both 5 and 11")
else:
    print("does not meet the condition")