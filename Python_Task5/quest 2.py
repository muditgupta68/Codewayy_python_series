# ------------------------------------------------START-----------------------------------------------------------------
# importing modules
import math

# initialising area
thisLst = [1,3,8,9,2,5,7,6,4,10]
thisTup = (1,3,8,9,2,5,7,6,4,10)
thisSet = {1,3,8,9,2,5,7,6,4,10}
thisDict = {'name':'mudit', 'age':19, 'college':'amity'}

# ----------------------------------------------SORTINGS----------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------Sorting the List---------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# using function
sortLst = sorted(thisLst)
print("The new sorted list is: ", sortLst)

# using method
thisLst.sort()
print("The list is sorted: ",thisLst)
thisLst.sort(reverse=True)
print("The list is reversed sorted: ",thisLst)
print("\n")

# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------Sorting the tuple--------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

print("The tuple is before sorted: ",thisTup)
sortTup = sorted(thisTup)
print("The tuple is after sorted: ",sortTup)
print("\n")

# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------Sorting the sets---------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

print("The sets are before sorted: ",thisSet)
sortSet = sorted(thisSet)
print("The sets are after sorted: ",sortSet)
print("\n")

# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------Sorting the Dictionary---------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

print("The dictionaires are before sorted: ",thisDict)
sortDict = sorted(thisDict)
print("The dictionaires are after sorted: ",sortDict)
print("\n")

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------MATHS FUNCTION----------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# power function
num = int(input("Enter the value\n"))
power = int(input("Enter the power\n"))
print("The power of ",num," is: ",pow(num,power),'\n')

# maximum number in list
print("The maximum value in the list is: ",max(thisLst),'\n')

# minimum number in list
print("The minimum value in the list is: ",min(thisLst),'\n')

# squaring number
print("The square root of ",num," is: ",math.sqrt(num),'\n')

# Rounding up numbers
print("the round up of number 1.5 using ceil is : ",math.ceil(1.5),'\n')
print("the round up of number 1.5 using floor is : ",math.floor(1.5),'\n')

# ---------------------------------------------------END----------------------------------------------------------------
