num1 = int(input("Enter a value for num1:"))
num2 = int(input("Enter a value for num2:"))
operation = input("Enter the operation add/sub/mul/div:")
if operation == "add":
    print(num1+num2)
elif operation=="sub":
    if num1>num2:
        print(num1-num2)
    else:
        print(num2-num1)
elif (operation == "mul"):
    print(num1*num2)
elif operation == "div":
    if num1!=0 and num2!=0:
        print(num1/num2)
    else:
        print(0)
else:
    print("Invalid operation")