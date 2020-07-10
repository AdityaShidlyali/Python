# tuples are also one of the data structure in pthon 
# unlike list the tuples are immutable means the elemnts cannot be delted, added, altered in tuples
# the tuples are faster than lists
# tuples are only used only when the data cannot be changed

# insert() append() pop() remove() these methods are not applicable for tuples

# tuples are decleared using parenthesis ()

tuple_1 = tuple()
print(type(tuple_1))

# we can also store the mixed datatyped elements as well in tuple
tuple_1 = ("Hello", 1, 3, 5)
print(tuple_1)


# indexing and slicing remains the same in the tuples as in lists
print(tuple_1[1:3])
print(tuple_1[::-1])

# methods applied for tuples are
# count() index() len()
print("Total number of specified elements are : ", tuple_1.count(3))
print("Index of the element 3 : ", tuple_1.index(5))
print("The size of the tuple_1 is : ", len(tuple_1))