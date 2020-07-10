# there are two types of string formatting

name, age = "Aditya Shidlyali", 20

# 1st one is Python 3 string formatting : {} are the placeholders
print("Your name is {} and your age is {} ".format(name, age))
# we can also change the indexing of the placeholders and indexong starts with 0, 1, 2, 3....
print("Your name is {1} and your age is {0}".format(name, age))

# 2nd one is Python 3.6 string formatting :
print(f"Your name is {name} and your age is {age}") # simply invoke the f before the string starts