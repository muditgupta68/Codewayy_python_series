# ------------------------------------------------------START-----------------------------------------------------------

# data initialisation
strngInp = input("enter the string\n")
strLen = len(strngInp)
countAt = 0

# logic
for i in range(0,strLen,1):
    if strngInp[i] == 'a' or strngInp[i] == 'A':
        if strngInp[i+1] == 't' or strngInp[i+1] == 'T':
            if strngInp[i+2] == ' ':
                countAt = countAt + 1
    else:
        continue

# printing
print("The number of at in the string are: ", countAt)

# -----------------------------------------------------END--------------------------------------------------------------
