# function which returns two values
# basically it dosent returns two defferent values it returns tuple with two or more values
# after returning the tuple we can unpack the tuple to store the elements in different variables

def func (data_1, data_2) :
    add = data_1+data_2
    multiply = data_1*data_2
    tuple_1 = (add, multiply) # however we replace this line with tuple_1(data_1+data_2, data_1*data_2)
    return tuple_1

# we can print the multiple values at once
print(func(2,3))

# we can also unpack the tuple by storing its values in different variables
addition, multiplicatoin = func(2,3)
print(addition, multiplicatoin)