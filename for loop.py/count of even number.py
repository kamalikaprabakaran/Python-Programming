# Count of even number between two numbers
num1 = int(input("Enter a value for num1:"))
num2 = int(input("Enter a value for num2:"))
count = 0
for i in range(num1,num2+1):
    if i%2==0:
        count+=1
print("Count of even number is:", count)