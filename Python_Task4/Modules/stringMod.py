# -----------------------------------------------------------------------------------------------------------------------

def midChar(strng):
    lenStrng = 0
    for i in strng:
        lenStrng = lenStrng + 1
    midLen = lenStrng // 2
    if lenStrng%2 != 0:
        midStrng = strng[midLen]
        print("The middle of the character of your string ", strng, " is: ", midStrng)
    else:
        midStrng = strng[midLen-1]+strng[midLen]
        print("The middle of the character of your string ", strng, " is: ",midStrng)

def vowlStrng(strng):
    lenStrng = 0
    for i in strng:
        lenStrng = lenStrng + 1
    count = 0
    for a in range(0,lenStrng,1):
        if strng[a] == 'a' or strng[a] == 'i' or strng[a] == 'o' or strng[a] == 'u' or strng[a] == 'e':
            count = count + 1
    print("The number of vowels in the string is: ",count)

def vowlData(dataInput):
    count1 = 0
    lenData = 0
    for i in dataInput:
        lenData = lenData + 1
    for i in range(0,lenData,1):
        if dataInput[i] == 'a' or dataInput[i] == 'i' or dataInput[i] == 'o' or dataInput[i] == 'u' or dataInput[i] == 'e':
            count1 = count1 + 1
    print("The number of vowels in the data is : ",count1)


def lenDat(strng):   # length of string
    counter = 0
    for i in strng:
        counter = counter + 1
    print("The length of the string is :",counter)

def strngDaata(dataInput):
    counting = 0
    lenData = 0
    for i in dataInput:
        lenData = lenData + 1
    for i in range(0,lenData,1):
        if dataInput[i] != " ":
            counting = counting + 1
    print("The number of words in the string are :", counting)

# -----------------------------------------------------------------------------------------------------------------------







