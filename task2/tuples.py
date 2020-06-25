name = ('mudit','deepak','riya','rahul','mudit')  
# tuple initiated
print(name)

# tuples are immutable whereas lists are mutable

# counting function
total = name.count('mudit')  
# count() will count the data in the tuple
print("total count of mudit in the tuple :",total)

# converting tuple into list
lname = list(name)
print(lname)

# length function
length = len(name)
# len() will print the length of the tuple
print(length)  

# index function
x = name.index('riya')  
# index() will tell the index of the data
print(x)

lst = [1,2,3,4,5,6]  # list initiated
print(lst)
# converting list into tuple
tname = tuple(lst)  
# list is converted to tuple
print(tname)



