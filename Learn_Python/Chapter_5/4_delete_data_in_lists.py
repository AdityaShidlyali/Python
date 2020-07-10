# to delete the data in the list there are two methods
# 1st is based on the index number and 2nd one is based on the element specified

# 1st method
list_1 = ["apple", "mango", "chickoo", "banana", "grapes"]
del list_1[2]
print(list_1)

list_1.pop(2) # 2 here is the index number of the list
print(list_1) # without mentioning the index number the pop() method deletes the element from the last index

# 2nd method
list_1.remove("grapes")
print(list_1)