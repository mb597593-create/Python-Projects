num1= float(input("Enter first value:"))
Operator=input("Enter operator(+,-,*,/):")
num2= float(input("Enter Second value:"))

if Operator=="+":
    print("Result:",num1+num2)
elif Operator=="-":
    print("Result:",num1-num2)
elif Operator=="*":
    print("Result:",num1*num2)
elif Operator=="/":
    if num2!=0:
        print("Result:",num1/num2)
    else:
        print("Cannot divide by zero")
else:
    print("invalid Operator")
