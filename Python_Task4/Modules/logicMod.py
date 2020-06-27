# -----------------------------------------------------------------------------------------------------------------------

def andOp(x):
    if x >= 1 and x <= 100:
        print("Is data between 1 and 100(using AND): \nTrue")
    else:
        print("Is data between 1 and 100(using AND): \nFalse")


def orOP(x):
    print("Is data between 1 and 100(using OR): ")
    print(x >= 1 or x <= 100)


def notOP(x):
    print("Is data between 1 and 100(using NOT): ")
    print(not (x >= 1 and x <= 100))

# -----------------------------------------------------------------------------------------------------------------------
