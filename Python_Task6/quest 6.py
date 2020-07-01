# ------------------------------------------------------START-----------------------------------------------------------

# function initialisation
def findType(n):
    divSum = 0
    for i in range(1, n, 1):
        if n % i == 0:
            divSum = divSum + i
    if divSum == n:
        return 0
    elif divSum < n:
        return 1
    else:
        return -1


# main
n = int(input("enter the times you want to enter the data\n"))
for i in range(0,n,1):
    n = int(input("Enter the number\n"))
    divType = findType(n)
    if divType == 0:
        print("Perfect Number\n")
    elif divType == 1:
        print("Deficient Number\n")
    else:
        print("Abundant Number\n")

# -----------------------------------------------------END--------------------------------------------------------------
