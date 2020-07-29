# set datatype
# unordered collection of unique elements.
# we can have the integer, float and as well as string in the set DS.
# (NOTE : if there is 1.0 and 1 in the set, then set treats them as single element).
# (NOTE : if we want to store the list or any other data structures in the set it will throw an error).

# example : 
s = {1, 2, 3, 4}
print(s)

# removing the duplicate elements using set.
l = [1, 2, 2, 3, 4, 4]
s2 = set(l)
print(s2)

# we can also convet list to set to remove the duplicate elements and then we can also convert the set to the list again.
s2 = list(set(l))
print(s2)

# methods used in set : 
# 1. add()
s.add(100) # will insert the elements in unordered fashion in the set.
print(s)

# 2. remove(element)
s.remove(100) # if the element is not in the set which is to be removed, then it gives the keyerror.
print(s)

# 3. discard()
s.discard(200) # this will not give the error if the element is absent though.
print(s)

# 4. copy()
s1 = s.copy() # this will create the deep copy of the desired set to the new set
print(s1)