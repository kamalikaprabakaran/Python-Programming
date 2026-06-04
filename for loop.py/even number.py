# Even number between two numbers
num1 = int(input("Enter a value for num1:"))
num2 = int(input("Enter a value for num2:"))
for i in range(num1,num2+1):
    if i%2 == 0:
        print(i, "is Even number.")