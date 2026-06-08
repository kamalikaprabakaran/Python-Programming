# Sum of numbers and average 
num = int(input("Enter a number:"))
count=0
for i in range(num+1):
    count+=i
print("Sum of number is : ", count)

average = count/num
print("Average of numbers is:",average)