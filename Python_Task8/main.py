# module initialised
import classMod
import time
# --------------------------------------------START---------------------------------------------------------------------

# user-admin menu bar
print('\n')
print('◖Welcome◗\n◎ You are:-\n')
print('\t* Admin')
print('\t* User\n')
choice = input('Enter the choice:\t')
print('\n')
choice = choice.lower()

# if choice is admin
# logic for admin
while choice == 'admin' or choice == '1':

    # admin entering no of students
    num = int(input('⚫ Enter the number of data of students you want to enter?\t'))

    # multiple list of objects creation
    # on the basis of no of students
    objLst = []
    for i in range(num):
        obj = classMod.course()
        objLst.append(obj)

    # calling functions via list of objects
    for j in objLst:
        j.studInput()
        j.fileDetail(1)
        j.crsOpt()
        j.gradeStud()
        j.ttnFee()
        j.gpaScr()
        j.filStud3()
        j.filStud4()
    print('\n')
    print('◖Welcome◗\n◎ You are:-\n')
    print('\t* Admin')
    print('\t* User\n')
    choice = input('Enter the choice:\t')
    print('\n')
    choice = choice.lower()

if choice == '2' or choice == 'user':
        # object initialised
        objct = classMod.course()

        # menu driven bar for user
        print('Greetings USER, ◖Welcome◗')
        time.sleep(3)
        print('\n')
        print(
            '--------------------------------------------MENU BAR--------------------------------------------------------')
        print('❶ List of Courses')
        print('➋ List of Students')
        print('❸ List Students & Enrollment')
        print('❹ Grade Report')
        print('⓿ Exit')
        print(
            '------------------------------------------------------------------------------------------------------------')
        print('\n')
        userInput = input("Enter the choice:\t")
        print('\n\n')
        while choice == '2' or choice == 'user':
            # displaying courses details
            if userInput == '1':
                time.sleep(3)
                objct.dispCourse1()

            # displaying students details
            elif userInput == '2':
                file = open('student.txt')
                time.sleep(3)
                print(file.read())
                file.close()

            # displaying student-enrollment data
            elif userInput == '3':
                file = open('disp3.txt')
                time.sleep(3)
                print(file.read())
                file.close()

            # displaying tution fee paid students
            elif userInput == '4':
                file = open('disp4.txt')
                time.sleep(3)
                print(file.read())
                file.close()
            else:
                exit()

            time.sleep(5)
            # re-driving menu user bar
            print('\n')
            print('hello USER, ◖Welcome◗')
            print('\n')
            print(
                '--------------------------------------------MENU BAR--------------------------------------------------------')
            print('❶ List of Courses')
            print('➋ List of Students')
            print('❸ List Students & Enrollment')
            print('❹ Grade Report')
            print('⓿ Exit')
            print(
                '------------------------------------------------------------------------------------------------------------')
            print('\n')
            userInput = input("Enter the choice:\t")
            print('\n\n')

# if choice is to exit
# program ends
if choice == 'exit' or choice == '3':
    print('▶\t THANKYOU!')
    exit()

# ----------------------------------------------------------END---------------------------------------------------------










