# we decalear the function with def keyword
"""
Syntax is : 
def function_name (parameters) :
    statement
"""

def add (data_1, data_2) :
    return data_1 + data_2

def fun () :
    pass # for epmty function we must and should invoke the pass statement

num_1 = int(input("Enter 1st number : "))
num_2 = int(input("Enter 2nd number : "))
print("The sum is : ", add(num_1, num_2))

first_name = input("Enter your first name : ")
second_name = input("Enter your second name : ")
print("Your full name is : ", add(first_name, second_name))

print(fun) # empty function returns none value