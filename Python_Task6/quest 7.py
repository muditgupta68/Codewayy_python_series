# ------------------------------------------------------START-----------------------------------------------------------

def check_marks(m):
    if m >= 90:
        return print(True)
    elif m < 90:
        raise Exception("Error! Data could not reach the limit! \nTry again!!")


# main
n = int(input("enter the times you want to enter the data\n"))
for i in range(0,n,1):
    marks = int(input("Enter the marks\n"))
    check_marks(marks)

# -----------------------------------------------------END--------------------------------------------------------------
