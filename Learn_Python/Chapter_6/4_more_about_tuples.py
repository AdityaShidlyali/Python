tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple_2 = tuple(range(1, 11)) # however we can do this too for lists but replace the tuple keyword with list
print(tuple_1)
print(tuple_2)

tuple_1 = str((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(tuple_1) # otput is in the form of tuple but when we check the type it shows string
print(type(tuple_1))
# the above step can be done as well for the lists too