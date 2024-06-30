num1 = int(input("enter num1 : "))
num2 = int(input("enter num2 : "))
num3 = int(input("enter num3 : "))

if(num1 >= num2 and num1 >= num3):
    print("num1 is greater number")
elif(  num2 >= num3):
    print("num2 is greater number")
else:
    print("num3 is greater number")