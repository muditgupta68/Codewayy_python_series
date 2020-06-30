# ------------------------------------------------------START-----------------------------------------------------------

# list initialised
lst = [(),(),('mudit','gupta'),('Raj','Rahul'),(),('Sushant','singh','rajput'),()]
print("\nThe list with empty tuple \n",lst,'\n')

# new list initialised
newLst = []

# removed list from empty tuple
for i in lst:
    if i != ():
        newLst.append(i)
print("The empty tuples are removed successfully!!\n",newLst)

# -----------------------------------------------------END--------------------------------------------------------------
