# ----------------------------------------------------START-------------------------------------------------------------

try:
    print(sumNum)
    file = open('fle.txt')
    if sum == '\0':
        raise Exception
    file.close()
except FileNotFoundError:
    print("the file doesnt exist!! ")
    print('ERROR 606')

except Exception:
    print('variable is NOT defined!')
    print('ERROR 607')

else:
    print(file.read())

finally:
    print("thankyou!")

# ----------------------------------------------------END---------------------------------------------------------------
