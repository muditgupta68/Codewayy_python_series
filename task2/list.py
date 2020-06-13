fruit = ["grapes","apple","banana",'peach','mango']     # list of fruits
print(fruit)   # printing the list

# Changing values
fruit[3] = 'oranges'  # this statement will make change in list
print(fruit)

# len function
print(len(fruit))   # len() function counts the number of data in the list

# append function
fruit.append("peach")  # append() function will add the data in the end
print(fruit)

# insert function
fruit.insert(2,"chiku")  # insert() function will add the data to the desired index
print(fruit)

# remove function
fruit.remove("grapes")  # remove() function will remove the desired data from list
print(fruit)

# pop function
fruit.pop(2)  # pop() will remove the of the desired index
print(fruit)

# sort function
fruit.sort()  # sort() will sort the list
print(fruit)

# extend function
fruit.extend("chiku")  # extend() will add the letters of the data or list at the end
print(fruit)

# using min()
minimum = min(fruit) # min() finds the minimum data in the list
print(minimum)

# using max()
maximum = max(fruit) # max() finds the maximum data in the list
print(maximum)

# clearing function
fruit.clear()  # clear() will clear the data
print(fruit)