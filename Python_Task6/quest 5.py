# ------------------------------------------------------START-----------------------------------------------------------

# string user-initialised
inputStrng = input("Enter the string\n")

# string length
strngLen = len(inputStrng)

# values initialised
wordCount = 1

# logic
for i in range(0,strngLen,1):
    if inputStrng[i] == " ":
        wordCount = wordCount + 1
    elif inputStrng[i] == '\0':
        break
    else:
        continue

# printing data according to user-initialised string
print("The number of words in the entered string is : ",wordCount)

# ------------------------------------------------------END-------------------------------------------------------------
