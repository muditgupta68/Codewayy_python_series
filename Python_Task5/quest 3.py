# ----------------------------------------------------START-------------------------------------------------------------
#                                               reading from file
# ----------------------------------------------------------------------------------------------------------------------

try:
    # opening file
    rdFile = open('cortana.txt')

except :
    # if file not opened, this message will prompt
    print("File doesnt exist, Try again later thankyou")

else :

    # reading the file upto 5 character
    print(rdFile.read(5))

    # reading the file line by line
    print(rdFile.readline())
    print(rdFile.readline())
    print(rdFile.readline())
    print(rdFile.readline())
    print(rdFile.readline())
    print(rdFile.readline())
    print(rdFile.readline())
    print(rdFile.read(5))

finally:
    # closing file
    rdFile.close()

# -------------------------------------------------------END------------------------------------------------------------
