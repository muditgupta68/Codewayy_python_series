car = {"brand":"ford",'year':1990,'model':'mustang','design':'sedan'}  # dictionary initiated
print(car)

# copy function
vehicle = car.copy()  
# copy() creates copy of dictionary
print(vehicle)

# pop function
car.pop('design')  
# pop() deleted the item of the key
print(car)

# accessing the item of key
mod = car['model']
print(mod)
mod1 = car.get('model')
print(mod1)

# adding data in the dictionary
car['color'] = 'black'
print(car)

# accessing values of dictionary car
val = car.values()
print(val)

# accessing all the keys in the dictionary
ke = car.keys()
print(ke)

# clear function
car.clear()
print(car)
vehicle.clear()
print(vehicle)
# the keys and values are deleted from the dictionary




