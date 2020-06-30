# ------------------------------------------------------START-----------------------------------------------------------

# string user-initialisation
strngIn = input("Enter the string \n")

# string length
strngLen = len(strngIn)

# initialising values
upper = 0
lower = 0

# logic
for i in range(0,strngLen,1):
    if strngIn[i] >= 'A' and strngIn[i]<= 'Z':
        upper = upper + 1
    elif strngIn[i] >= 'a' and strngIn[i]<= 'z':
        lower = lower + 1
    else :
        continue

# printing data according to user-initialised string
print("The number of Upper letter is the string entered are : ",upper)
print("The number of Lower letter is the string entered are : ",lower)

# ----------------------------------------------------END---------------------------------------------------------------
