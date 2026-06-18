def staircase(n):
    for row in range(1,n+1):
        for space in range(n-row):
            print(" ",end='')
        for hash in range(row):
            print("#",end='')
        print()
n =int(input("Enter a number:"))
print(staircase(n))
