# Get numbers from user and display them in a list
num = int(input("Enter the number:"))
arr = []
for i in range(num):
    element = int(input("Enter a value:"))
    arr.append(element)
print("The number are:", arr)

