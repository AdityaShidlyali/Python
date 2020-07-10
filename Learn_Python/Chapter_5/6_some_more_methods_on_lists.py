# count() method
# sort() method
# sorted() method
# reverse() method
# clear() method
# copy() method

# count()
list_1 = ['orange', 'apple', 'grapes', 'mango', 'cherry', 'chickoo', 'kiwi', 'orange']
print(list_1.count('orange'))

# sort()
numbers = [4,12,456,634,12,10]
numbers.sort() # this method not only sorts the numbers, this also sorts the strings in alphabetical order
print(numbers)

# sorted()
numbers = [4,12,456,634,12,10]
print(sorted(numbers)) # this will not sort and modify the list into sorted order but only prints the list in the sorted order
print(numbers) # again the numebrs list remains as it is

# reverse()
list_1.reverse() # this will reverse all the elements in the list in the reverse order and modifies the list into the reverse order
print(list_1)

#clear() 
list_1.clear()
print(list_1) # this will clear or delete all the data in the list

#copy()
numbers_copy = numbers.copy()
print(numbers_copy)

# the copy method clones the lists to two different list with the different variable names
numbers_copy[0] = 100
print(numbers_copy)
print(numbers) # numbers[0] != 100 when you print it

# we can copy the list using the following method also
numbers_copy = numbers[:]
print(numbers_copy)

# the assignment sign will not copy the list to another list but both the list point to the same list
# this is called aliasing
numbers_copy = numbers
numbers_copy[0] = 100
print(numbers) # both the lists get modified
print(numbers_copy)