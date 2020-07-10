list_1 = [1, 12, 14, 4, 5, 6, 23, 543, 5]

# index() method
# this has got the three numebr of arguments index(value_to_be_searched, start_value, stop_value)

print(list_1.index(5)) # this returns the value of the first element as 5
print(list_1.index(5, 5)) # it returs the position of the value in the list

popped_element = list_1.pop(3) # this not only deleted the element in the list this element also returns the value which is deleted
print("The popped item is : ", popped_element)