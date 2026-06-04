# Multiplication tables
num = int(input("Enter a number:"))
end = int(input("Enter the end number of the tables:"))
for i in range(1,end+1):
    print(num,"*",i,"=",num*i)