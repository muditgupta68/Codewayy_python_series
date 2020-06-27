# ----------------------------------------------------START-------------------------------------------------------------
# function to check prime
def checkPrime(number):
    if number > 1:
        for i in range(2,number):
            if (number % i) != 0:
                return number

# initialising the size of matrix
matSize = int(input("enter the size of matrix\n"))
primMat = []
print("Enter the data of the matrix")

# input value from user
for i in range(0, matSize, 1):
    lst = []  # initialising new list
    for j in range(0, matSize, 1):
        lst.append(int(input()))
    primMat.append(lst)

# printing matrix
for i in range(0, matSize, 1):
    for j in range(0, matSize, 1):
        print(primMat[i][j], end=" ")
    print("\n")

# searching the prime number

print("Prime numbers in the matrix")
for i in range(matSize):
    for j in range(matSize):
        if checkPrime(primMat[i][j]):
            print(primMat[i][j])

# -------------------------------------------------------------END------------------------------------------------------
