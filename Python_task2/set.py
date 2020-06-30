c_lang = {'C++','java','django','python','CS'}  
#set initiated
print(c_lang)

# add function
c_lang.add("HTML")  
# add() will add the desired data
print(c_lang)

# remove function
c_lang.remove("HTML")  
# remove() deletes the data from the set
print(c_lang)

# copy function
language=c_lang.copy()  
# copy() creates a copy of set
print(language)

# pop function
c_lang.pop()  
# pop() deletes the data randomly
print(c_lang)

# length function
length = len(language)  
# len() tells the length of the set
print(length)

# clearing the set
c_lang.clear()
print(c_lang)
language.clear()
print(language)
# clear(), removes the data in the respective sets


