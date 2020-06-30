# -----------------------------------------------------START------------------------------------------------------------

# function initialised

def speedCheck(speed):
    if 70 > speed:
        print("OK")
        print('\n')
    else:
        demPoint = (speed - 70) / 5
        if demPoint > 12:
            print("LICENSE SUSPENDED!!")
            print("You overspeeded! The demerit points are: ",demPoint)
            print('\n')

        elif 12 >= demPoint >= 10:
            print("WARNING!! your license is on verge to get suspended!")
            print("The total number of demerit points are: ",demPoint)
            print('\n')
        else:
            print("The total number of demerit points are: ",demPoint)
            print('\n')


# ----------------------------------------------------------------------------------------------------------------------

# input speed


n = int(input("enter the times you want to enter the data\n"))
for i in range(0,n,1):
    speed = int(input("Enter the speed\n"))
    speedCheck(speed)

# -------------------------------------------------END------------------------------------------------------------------
