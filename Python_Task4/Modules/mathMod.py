# -----------------------------------------------------------------------------------------------------------------------

def sqNum(num1):
    sqNumber = num1 ** 2
    print("The square of the ",num1,' is: ',sqNumber)


def maxNum(lst):
    maxNo = lst[0]
    for i in lst:
        if maxNo < i:
            maxNo = i
    print("The maximum number is: ", maxNo)


def minNum(lst):
    minNo = lst[0]
    for i in lst:
        if minNo > i:
            minNo = i
    print("The minimum number is: ", minNo)


def sumNum(lst):
    sumNo = 0
    for i in lst:
        sumNo = sumNo + i
    print("The sum of the list is: ",sumNo)


# -----------------------------------------------------------------------------------------------------------------------