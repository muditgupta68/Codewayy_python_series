#-----------------------------------------------------START-------------------------------------------------------------
#-----------------------------------------------DEFINING FUNCTIONS------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
# function for name having middle name

def fullName(firstName,middleName,lastName):
    return (firstName + " " + middleName + " " + lastName)
#-----------------------------------------------------------------------------------------------------------------------
# functions for name having onlu first and last name

def full_Name(firstName,lastName):
    return (firstName + " " + lastName)
#-----------------------------------------------------------------------------------------------------------------------
# functions for total marks

def totMarks(LstoMks):
    totalMarks = sum(LstoMks)
    return (totalMarks)
#-----------------------------------------------------------------------------------------------------------------------
# functions for percentage scored

def percMarks(tMark,Mks):
    perMark = tMark/Mks
    return(perMark)
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

def Master(firstName,middleName,lastName,LstoMks,tMark,Mks,Percentage):
    print("\n\n")
    print("-------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------SCORECARD!-------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------")
    if middleName != "":
        print("Name: ",fullName(firstName, middleName, lastName))
    else:
        print("Name: ",full_Name(firstName, lastName))
    print("Total Marks Obtained: ",totMarks(LstoMks))
    print("Percentage obtained: ",percMarks(tMark,Mks))
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
    firstName = input("Enter your first name:")
    middleName = input("Enter your middle name:")
    lastName = input("Enter your last name")

else:
    firstName = input("Enter your first name:")
    lastName = input("Enter your last name")
    middleName = ""

Mks = int(input("Enter the number of marks you want to enter:-\n"))
print("Enter the Marks you want to enter")
LstoMks = []
for i in range(0,Mks,1):
    Marks = int(input(i+1))
    LstoMks.append(Marks)
tMark = totMarks(LstoMks)
Percentage = percMarks(TMark,Mks)
Grade(Percentage)
Master(firstName,middleName,lastName,LstoMks,tMark,Mks,Percentage)

#-----------------------------------------------------------END---------------------------------------------------------
