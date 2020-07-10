# we use various essential methods on lists
# methods are : 
# 1. append()
# 2. extend()
# 3. insert()

list_1 = ["apple", 'grapes']
list_2 = ["cherry", "chikoo"]

new_list = list_1 + list_2 # a simple + is used to add the two lists
print(new_list)

list_1.extend(list_2) # it will add the elements of other list to existing list
print(list_1)

# index method has got two arguments to be passed insert (index_no_to_insert_list, list_variable)
list_1.insert(2, list_2)
print(list_1) # add one more list inside the existing list based on the index number specified

list_1.append(list_2)
print(list_1) # this will add the another list to existing list at the end of the list