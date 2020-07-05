# -----------------------------------------------------START------------------------------------------------------------
# class initialisation
class student:
    def __init__(self):
        self.fstName = 'ABC'
        self.lstName = 'XYZ'
        self.clgName = '???'
        self.branch = 'no data'
        self.totMarks = -1
        self.percScrd = 0
        self.gradeScored = 'E'

    def disName(self):
        self.fstName = input("Enter the first name: \n")
        self.lstName = input("Enter the last name: \n")

    def disClg(self):
        self.clgName = input("Enter the name of college: \n")
        self.branch = input("Enter the branch of your program:\n")

    def disMarks(self):
        lstMarks = []
        self.tot = int(input("Enter the number of marks you want to enter\t"))
        for i in range(0,self.tot,1):
            marksScored = int(input("Enter the marks\t"))
            lstMarks.append(marksScored)
            self.totMarks = sum(lstMarks)

    def disPerc(self):
        self.percScrd = self.totMarks / self.tot

    def disGrade(self):
        if self.percScrd >= 90:
            self.gradeScored = 'A'
        elif self.percScrd >= 80:
            self.gradeScored = 'B'
        elif self.percScrd >= 70:
            self.gradeScored = 'C'
        elif self.percScrd >= 60:
            self.gradeScored = 'D'
        else:
            self.gradeScored = 'F'

    def Master(self):
        print('\n\n\tSCORECARD\n')
        print("NAME:\t", self.fstName + ' ' + self.lstName)
        print("COLLEGE:\t", self.clgName)
        print('BRANCH:\t', self.branch)
        print('MARKS:\t', self.totMarks)
        print('PERCENTAGE SCORED:\t', self.percScrd)
        print('GRADE SCORED:\t', self.gradeScored)
        print("----------------------------------------------------------------------------------------------------\n\n")

# Void main
# list of object initialised
objLst = []

# initialising object of the class
for i in range(0,5,1):
    obj = student()
    objLst.append(obj)

# constructor initialisation
objLst[0].Master()

# calling function
for i in objLst:
    i.disName()
    i.disClg()
    i.disMarks()
    i.disPerc()
    i.disGrade()
    i.Master()

# ----------------------------------------------------------END---------------------------------------------------------