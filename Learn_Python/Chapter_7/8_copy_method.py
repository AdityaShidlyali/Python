# copy method in python dictionary

d = {'name' : 'Aditya', 'age' : '21'}
d2 = d.copy()
print(d2)

# if we assign the dictionaries like d2 = d then the both the variables are pointing to same dictionaries
# if we assign d2 = d whatever the changes made to d2 are reflected in d as well

# to check the if the dictionaries are same we can check that as well by following :
d = {'name' : 'Aditya', 'age' : '21'}
d2 = d
if d2 is d :
    print("true")
else :
    print("false")