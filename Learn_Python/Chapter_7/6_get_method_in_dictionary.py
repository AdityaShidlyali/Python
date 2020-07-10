# get method in python dictionaries
d = {'name' : 'Aditya', 'age' : '21'}
print(d['name'])

print(d.get('name'))
print(d.get('names'))

# check keys in the dictionary
if 'names' in d :
    print("Present")
else :
    print("not present")

# the above can also be done as :
if d.get('names') :
    print("Present")
else :
    print('not present')