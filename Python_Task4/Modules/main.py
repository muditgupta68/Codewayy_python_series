# ---------------------------------------------------START--------------------------------------------------------------
# ---------------------------------------------------MODULES------------------------------------------------------------
import mathMod
import stringMod
import logicMod
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------VOID MAIN---------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 1st nodule:-
"""
num1 = int(input("Enter the number whose square you want to find:- \n"))
mathMod.sqNum(num1)

lst = []    # empty list
n = int(input("Enter the number of data you want to enter\n"))
for a in range(0,n,1):
    print("Enter the data in the ",a," location")
    dataInpt = int(input(""))
    lst.append(dataInpt)
print("The list entered is: ",lst)

mathMod.maxNum(lst)
mathMod.minNum(lst)
mathMod.sumNum(lst)
"""
# ----------------------------------------------------------------------------------------------------------------------
# 2nd module:-

strng = input("Enter the string whose middle character you want to know \n")
stringMod.midChar(strng)
stringMod.vowlStrng(strng)
stringMod.lenDat(strng)
print("---------------------------------------------------------------------------------------")
dataInput = input("Enter the data\n")
stringMod.vowlData(dataInput)
stringMod.strngDaata(dataInput)
""""
# ----------------------------------------------------------------------------------------------------------------------
# 3rd Module:-

x = int(input("Enter the value\n"))
logicMod.andOp(x)
logicMod.orOP(x)
logicMod.notOP(x)
"""
# ----------------------------------------------------END---------------------------------------------------------------
