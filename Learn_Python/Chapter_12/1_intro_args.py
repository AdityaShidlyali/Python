# make flexible functions
# *operator
# *args

def total (a, b):
    return a+b

# this will give the error, to remove the errors we use *operator
# print(total(3, 4, 5, 6))

def tot_all(*args): # the args default are in the form of tuple
    total = 0 #(NOTE : according to the naming conventions in python after the * operator args must be written)
    for num in args :
        total += num
    print(total)

tot_all(1, 2, 3, 4, 5, 6, 7)