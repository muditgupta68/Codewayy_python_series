#-----------------------------------------------------START-------------------------------------------------------------
#-----------------------------------------------DEFINING FUNCTIONS------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
# function for name having middle name

def FullName(FirstName,MiddleName,LastName):
    return (FirstName + " " + MiddleName + " " + LastName)
#-----------------------------------------------------------------------------------------------------------------------
# functions for name having onlu first and last name

def Full_Name(FirstName,LastName):
    return (FirstName + " " + LastName)
#-----------------------------------------------------------------------------------------------------------------------
# functions for total marks

def TotMarks(LstoMks):
    TotalMarks = sum(LstoMks)
    return (TotalMarks)
#-----------------------------------------------------------------------------------------------------------------------
# functions for percentage scored

def PercMarks(TMark,Mks):
    PerMark = TMark/Mks
    return(PerMark)
#-----------------------------------------------------------------------------------------------------------------------
# functions for grading

def Grade(Percentage):
    if Percentage >= 95:
        return ('A')
    elif Percentage >= 85 and Percentage <= 95:
        return ('B')
    elif Percentage >= 75 and Percentage <= 85:
        return ('C')
    elif Percentage >= 65 and Percentage <= 75:
        return ('D')
    else:
        return ('F')
#-----------------------------------------------------------------------------------------------------------------------
# Master function

def Master(FirstName,MiddleName,LastName,LstoMks,TMark,Mks,Percentage):
    print("\n\n")
    print("-------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------SCORECARD!-------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------")
    if MiddleName != "":
        print("Name: ",FullName(FirstName, MiddleName, LastName))
    else:
        print("Name: ",Full_Name(FirstName, LastName))
    print("Total Marks Obtained: ",TotMarks(LstoMks))
    print("Percentage obtained: ",PercMarks(TMark,Mks))
    print("Grade obtained: ",Grade(Percentage))
    print("-------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------THANKYOU!--------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------VOID MAIN---------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

print("Do you have Middle name?")
Res = input("yes/no:-\n")
if Res == "yes":
    FirstName = input("Enter your first name:")
    MiddleName = input("Enter your middle name:")
    LastName = input("Enter your last name")

else:
    FirstName = input("Enter your first name:")
    LastName = input("Enter your last name")
    MiddleName = ""

Mks = int(input("Enter the number of marks you want to enter:-\n"))
print("Enter the Marks you want to enter")
LstoMks = []
for i in range(0,Mks,1):
    Marks = int(input(i+1))
    LstoMks.append(Marks)
TMark = TotMarks(LstoMks)
Percentage = PercMarks(TMark,Mks)
Grade(Percentage)
Master(FirstName,MiddleName,LastName,LstoMks,TMark,Mks,Percentage)

#-----------------------------------------------------------END---------------------------------------------------------