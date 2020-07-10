list_1 = ['orange', 'apple', 'grapes', 'mango', 'cherry', 'chickoo', 'kiwi', 'orange']
list_2 = ['orange', 'apple', 'grapes', 'mango', 'cherry', 'chickoo', 'kiwi', 'orange']
list_3 = ['orange', 'apple', 'grapes', 'mango']

print(list_1 == list_2) # prints true because all the elements are same in the list

print(lsit_1 == list_3) # prints false because the elements in the list_1 are not same as in the list_3

print(list_1 is list_2) # prints flase becasue both lists are pointing to different memory location

list_1 = list_2 # you can see what happens when we do this step in the previous file
print(list_1 is list_2) # now the lists point to the same memory location so the result is true