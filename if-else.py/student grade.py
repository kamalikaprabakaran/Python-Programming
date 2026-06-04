# Get mark from the user and determine if they are a good, average or poor student.``
mark = int(input("Enter the mark:"))
if (mark<35):
    print("Poor student")
elif(mark>53 and mark<70):
    print("Average student")
else:
    print("Good student")