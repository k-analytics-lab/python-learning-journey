ops = input("Enter a operator (+,-,*,/) : ")
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

if ops=="+":
    print(num1+num2)
elif ops=="-":
    print(num1-num2)
elif ops=="*":
    print(num1*num2)
elif ops=="/":
    print(num1/num2)
else:
    print("Enter a valid operator or number")
