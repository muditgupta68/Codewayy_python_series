# ----------------------------------------------------START-------------------------------------------------------------
#                                               writing into file
# ----------------------------------------------------------------------------------------------------------------------
# writing the file
wrtFile = open('file.txt','w')
strng = input("enter the string :\n")
wrtFile.write(strng)
wrtFile.close()

# reading the file
rdFile = open('file.txt')
print(rdFile.readline())

# -------------------------------------------------------END------------------------------------------------------------

