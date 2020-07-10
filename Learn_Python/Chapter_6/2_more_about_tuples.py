# looping in tuple 
tuple_1 = (1, 3, 5, 7, 11)

for i in tuple_1 :
    print(i, end = ' ') # we can use while loop too


print('\n') # simply used to print the further things on the new line

# tuple with one element :
num = (1)
print(type(num))
num = (1,) # just place one comma after the single element in tuple
print(type(num))
word = ("Hello")
print(type(word))
word = ("Hello", )
print(type(word))

# tuple without bracket
tuple_1 = "Hello", "Aditya", "Shidlyali" # assigning elements seperating them with comma becomes tuple
print(type(tuple_1))

# tuple unpacking
data_1 , data_2, data_3 = (tuple_1) # or you can simply assign tuple_1
print(data_1, data_2, data_3)

# list inside tuple
tuple_1 = ("Hello", 2, 3.142, ["Aditya"])
tuple_1[3].append("Shidlyali") # we can do this to the list which is inside the tuple
print(tuple_1)

# some functions that can be performed on tuples are
tuple_1 = ( 12, 412, 12, 54, 34)
print("Maximum value : ", max(tuple_1))
print("Minimum value : ", min(tuple_1))
print("Total sum is : ", sum(tuple_1))
