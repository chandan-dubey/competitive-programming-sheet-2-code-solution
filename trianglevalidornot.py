angle1=int(input("enter angle 1 "))
angle2=int(input("enter angle 2 "))
angle3=int(input("enter angle 3 "))
if(angle1>0 and angle2>0 and angle3>0 and angle1+angle2+angle3==180):
    print("triangle is valid")
else:
    print("triangle is invalid")