# base class- person
class person:
    # constructor of person
    def __init__(self):
        self.frstName = 'ABC'
        self.lstName = 'XYZ'
        self.studID = 0
        self.fullName = '???'

    # input of student details
    def studInput(self):
        self.frstName = input('Enter the first name:\t')
        self.lstName = input('Enter the last name:\t')
        self.studID = int(input('Enter the Student ID:\t'))
        self.fullName = self.frstName + ' ' + self.lstName

    # writing the details of students
    # in student-text-file
    def fileDetail(self, s):
        file1 = open('student.txt', 'a')
        for i in range(0, s, 1):
            id = str(self.studID)
            file1.write(id)
            file1.write('\t\t\t\t\t')
            file1.write(self.fullName)
            file1.write('\n')
        file1.close()

    # reading out the details of students
    # from student-text-file
    def studOutpt2(self):
        file = open('student.txt')
        print(file.read())
        file.close()

# inherited class- student
# from base class- person
class student(person):
    # restricting the over-riding of constructor
    # of base class- person
    def __init__(self):
        person.__init__(self)
        self.paidTtn = 'null'
        self.feeValue = 0
        self.opt = 0
        self.gradeScr = []
        self.gpaScrd = 0
        # courses
        self.crs1 = 'Object-Oriented in C++'
        self.crs2 = 'Financial Engineering'
        self.crs3 = 'Discrete Mathematics'
        self.crs4 = 'Intro Social Science'
        self.crs5 = 'Intro Linear Algebra'
        self.crs6 = 'Fundamental English'
        self.crs7 = 'Fundamental Japanese'
        # course ID
        self.crsID1 = 1234
        self.crsID2 = 1235
        self.crsID3 = 1236
        self.crsID4 = 1237
        self.crsID5 = 1238
        self.crsID6 = 1239
        self.crsID7 = 1240
        # course credit
        self.crsCrdt1 = 3
        self.crsCrdt2 = 3
        self.crsCrdt3 = 3
        self.crsCrdt4 = 2
        self.crsCrdt5 = 3
        self.crsCrdt6 = 2
        self.crsCrdt7 = 2

    # tution fee paid confirmation
    # no of courses opted by the student
    def crsOpt(self):
        self.paidTtn = input('Did the student paid the fees: (y/n):\t')
        self.opt = int(input('Enter the number of course opted by the student (max:6):\t'))
        flag = 0
        # atmost can opt 6 courses.
        while flag == 0:
            if self.opt < 6:
                self.crsID = []
                for i in range(0, self.opt, 1):
                    inptID = int(input('Enter the Course ID:\t'))
                    self.crsID.append(inptID)
                flag = 1
            else:
                print('Try again!!')

    # Grading the student in the respective course
    def gradeStud(self):
        for i in range(0, self.opt, 1):
            print('Enter the grade scored for ', self.crsID[i])
            grd = input('\t')
            self.gradeScr.append(grd)

    # Tution fee calculation
    # of the respective student
    def ttnFee(self):
        self.crdtLst = []
        s = 0
        for j in self.crsID:
            if j == self.crsID1:
                s = s + self.crsCrdt1
                self.crdtLst.append(self.crsCrdt1)
            elif j == self.crsID2:
                s += self.crsCrdt2
                self.crdtLst.append(self.crsCrdt2)
            elif j == self.crsID3:
                s += self.crsCrdt3
                self.crdtLst.append(self.crsCrdt3)
            elif j == self.crsID4:
                s += self.crsCrdt4
                self.crdtLst.append(self.crsCrdt4)
            elif j == self.crsID5:
                s += self.crsCrdt5
                self.crdtLst.append(self.crsCrdt5)
            elif j == self.crsID6:
                s += self.crsCrdt6
                self.crdtLst.append(self.crsCrdt6)
            elif j == self.crsID7:
                s += self.crsCrdt7
                self.crdtLst.append(self.crsCrdt7)
        self.feeValue = 500 * s


    # GPA calculation
    # of the student
    def gpaScr(self):
        gradeValue = []
        mult = 0
        for i in self.gradeScr:
            if i == 'a' or i == 'A':
                gradeValue.append(4)
            elif i == 'b' or i == 'B':
                gradeValue.append(3)
            elif i == 'c' or i == 'C':
                gradeValue.append(2)
            elif i == 'd' or i == 'D':
                gradeValue.append(1)
            elif i == 'f' or i == 'F':
                gradeValue.append(0)
        for i in range(0,self.opt,1):
            mult = mult + (gradeValue[i] * self.crdtLst[i])
        totCrdt = sum(self.crdtLst)
        self.gpaScrd = mult/totCrdt


    # Writing the details
    # to disp3-text-file
    def filStud3(self):
        file = open('disp3.txt','a')
        file.write(str(self.studID))
        file.write('\t\t')
        file.write(self.fullName)
        file.write('\n')
        file.write('Course ID\t\tCourse Name\t\t\t\t Course Credit\t\t\t\t Grade')
        file.write('\n')
        for i in range(0,self.opt,1):
            if self.crsID[i] == self.crsID1:
                file.write(str(self.crsID1))
                file.write('\t\t')
                file.write(self.crs1)
                file.write('\t\t\t\t')
                file.write(str(self.crsCrdt1))
                file.write('\t\t\t\t\t\t')
                file.write(self.gradeScr[i])
                file.write('\n')

            elif self.crsID[i] == self.crsID2:
                file.write(str(self.crsID2))
                file.write('\t\t')
                file.write(self.crs2)
                file.write('\t\t\t\t')
                file.write(str(self.crsCrdt2))
                file.write('\t\t\t\t\t\t')
                file.write(self.gradeScr[i])
                file.write('\n')

            elif self.crsID[i] == self.crsID3:
                file.write(str(self.crsID3))
                file.write('\t\t')
                file.write(self.crs3)
                file.write('\t\t\t\t')
                file.write(str(self.crsCrdt3))
                file.write('\t\t\t\t\t\t')
                file.write(self.gradeScr[i])
                file.write('\n')

            elif self.crsID[i] == self.crsID4:
                file.write(str(self.crsID4))
                file.write('\t\t')
                file.write(self.crs4)
                file.write('\t\t\t\t')
                file.write(str(self.crsCrdt4))
                file.write('\t\t\t\t\t\t')
                file.write(self.gradeScr[i])
                file.write('\n')

            elif self.crsID[i] == self.crsID5:
                file.write(str(self.crsID5))
                file.write('\t\t')
                file.write(self.crs5)
                file.write('\t\t\t\t')
                file.write(str(self.crsCrdt5))
                file.write('\t\t\t\t\t\t')
                file.write(self.gradeScr[i])
                file.write('\n')

            elif self.crsID[i] == self.crsID6:
                file.write(str(self.crsID6))
                file.write('\t\t')
                file.write(self.crs6)
                file.write('\t\t\t\t\t')
                file.write(str(self.crsCrdt6))
                file.write('\t\t\t\t\t\t')
                file.write(self.gradeScr[i])
                file.write('\n')

            elif self.crsID[i] == self.crsID7:
                file.write(str(self.crsID7))
                file.write('\t\t')
                file.write(self.crs7)
                file.write('\t\t\t\t')
                file.write(str(self.crsCrdt7))
                file.write('\t\t\t\t\t\t')
                file.write(self.gradeScr[i])
                file.write('\n')

            else:
                pass

        file.write('GPA:\t')
        file.write(str(self.gpaScrd))
        file.write('\n')
        file.write('Tuition Fee:\t')
        file.write(str(self.feeValue))
        file.write('\n\n')
        file.close()

    # Writing the details
    # to disp4-text-file
    def filStud4(self):

        if self.paidTtn == 'yes' or self.paidTtn == 'y' or self.paidTtn == 'Y' or self.paidTtn == 'Yes' or self.paidTtn == 'YES':
            file = open('disp4.txt','a')
            file.write(str(self.studID))
            file.write('\t\t')
            file.write(self.fullName)
            file.write('\n')
            file.write('Course ID\t\tCourse Name\t\t\t\t Course Credit\t\t\t\t Grade\n')
            file.write('\n')
            for i in range(0, self.opt, 1):
                if self.crsID[i] == self.crsID1:
                    file.write(str(self.crsID1))
                    file.write('\t\t')
                    file.write(self.crs1)
                    file.write('\t\t\t\t')
                    file.write(str(self.crsCrdt1))
                    file.write('\t\t\t\t\t\t')
                    file.write(self.gradeScr[i])
                    file.write('\n')

                elif self.crsID[i] == self.crsID2:
                    file.write(str(self.crsID2))
                    file.write('\t\t')
                    file.write(self.crs2)
                    file.write('\t\t\t\t')
                    file.write(str(self.crsCrdt2))
                    file.write('\t\t\t\t\t\t')
                    file.write(self.gradeScr[i])
                    file.write('\n')

                elif self.crsID[i] == self.crsID3:
                    file.write(str(self.crsID3))
                    file.write('\t\t')
                    file.write(self.crs3)
                    file.write('\t\t\t\t')
                    file.write(str(self.crsCrdt3))
                    file.write('\t\t\t\t\t\t')
                    file.write(self.gradeScr[i])
                    file.write('\n')

                elif self.crsID[i] == self.crsID4:
                    file.write(str(self.crsID4))
                    file.write('\t\t')
                    file.write(self.crs4)
                    file.write('\t\t\t\t')
                    file.write(str(self.crsCrdt4))
                    file.write('\t\t\t\t\t\t')
                    file.write(self.gradeScr[i])
                    file.write('\n')

                elif self.crsID[i] == self.crsID5:
                    file.write(str(self.crsID5))
                    file.write('\t\t')
                    file.write(self.crs5)
                    file.write('\t\t\t\t')
                    file.write(str(self.crsCrdt5))
                    file.write('\t\t\t\t\t\t')
                    file.write(self.gradeScr[i])
                    file.write('\n')

                elif self.crsID[i] == self.crsID6:
                    file.write(str(self.crsID6))
                    file.write('\t\t')
                    file.write(self.crs6)
                    file.write('\t\t\t\t\t')
                    file.write(str(self.crsCrdt6))
                    file.write('\t\t\t\t\t\t')
                    file.write(self.gradeScr[i])
                    file.write('\n')

                elif self.crsID[i] == self.crsID7:
                    file.write(str(self.crsID7))
                    file.write('\t\t')
                    file.write(self.crs7)
                    file.write('\t\t\t\t')
                    file.write(str(self.crsCrdt7))
                    file.write('\t\t\t\t\t\t')
                    file.write(self.gradeScr[i])
                    file.write('\n')

                else:
                    pass

            file.write('GPA:\t')
            file.write(str(self.gpaScrd))
            file.write('\n')
            file.write('Tuition Fee:\t')
            file.write(str(self.feeValue))
            file.write('\n\n')
            file.close()
        else:
            pass

# inherited class- course
# from base class- student
class course(student):
    def __init__(self):
        student.__init__(self)

    # displaying list of courses
    def dispCourse1(self):
        print('Course ID\t\tCourse Name\t\t\t\t Course Credit')
        print(self.crsID1,'\t\t',self.crs1,'\t\t',self.crsCrdt1)
        print(self.crsID2,'\t\t', self.crs2, '\t\t    ', self.crsCrdt2)
        print(self.crsID3,'\t\t', self.crs3, '\t\t    ', self.crsCrdt3)
        print(self.crsID4, '\t\t', self.crs4, '\t\t    ', self.crsCrdt4)
        print(self.crsID5, '\t\t', self.crs5, '\t\t    ', self.crsCrdt5)
        print(self.crsID6, '\t\t', self.crs6, '\t\t    ', self.crsCrdt6)
        print(self.crsID7, '\t\t', self.crs7, '\t\t    ', self.crsCrdt7)

