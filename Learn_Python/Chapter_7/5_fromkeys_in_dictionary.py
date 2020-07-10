# fromkeys in dictionary python
# it is used to assign the distinct keys with same value

d = dict.fromkeys(['name', 'age', 'height'], 'unknown') # it can be list
print(d)

d = dict.fromkeys(('name', 'age', 'height'), 'unknown') # it can tuple as well
print(d)

d = dict.fromkeys("abc", 'unknown')
print(d) # the d dictionary will have a, b, c as distinct keys

d = dict.fromkeys(range(1, 10), 'unknown')
print(d) # this will have the 1 to 9 as distinct keys as unknown