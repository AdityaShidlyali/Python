"""
in python if any of flow control statements or looping statements or classes or methods(functions)
need to be invoked emptily then we need to invoke pass statement inside them
"""

age = input("Enter your age : ")
age = int(age)

if age >= 20 :
    pass # if this has not been not included, if we leave it empty then it throws EOF error

print("Hello")