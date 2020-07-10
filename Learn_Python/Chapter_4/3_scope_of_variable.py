def fun1() :
    x = 7
    return x

def fun2() :
    """not recommended to use global because the maintanance of the variable becomes difficult"""
    # using global we cannot change the variable which are outide the functions
    global x
    x = 4
    return x

x = 5 # we can declear this variable before the function or after the function to change the value as global variable

print(x)

print(fun1())

print(x)

print(fun2())

print(x) # the x value here is changed because the x value is globally changed by the fun2() function