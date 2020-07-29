s = {'a', 'b', 'c'}

# to check whether the element exist in the set :
if 1 in s :
    print("Present")
else :
    print("Not present")

# to print the elements of the set :
# it will print the elements of the set in the random order, everytime its run.
for i in s:
    print(i)

# union in set
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
union_set = s1 | s2
print(union_set)

# intersection in set
intersection_set = s1 & s2
print(intersection_set)