# list is one of the data structure in python used to store the multiple elements of different types
# we can store the mixture of the int float characters or string datas

# we create or define the list using square brackets -> []

numbers = [1,2.3,5.6,4] # declearation of the list
print(numbers)

numbers = [] # empty list
print(numbers)

mixed = ["Hello", 3.142, 5]
print(mixed) # list containing the different types of data

print(mixed[:2]) # list slicing is same as that of string slicing

print(mixed[0][0], mixed[0][3]) # we can slice the the list elements deeply too (here it return the H and l)

mixed[1:2] = {"one"}

print(mixed)