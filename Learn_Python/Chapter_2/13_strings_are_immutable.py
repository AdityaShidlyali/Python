name = "Aditya"
# name[0] = "a" this making throws error
print(name.replace("A", "a")) # this however prints the replaced string but the actual string is not changed see the next statement
print(name) # prints the actual string

# however we can change manipulate the actual string and assign it to another string
new_string = name.replace("A", "a")

# this shows that the strings are immutable means their characters cannot be changed

# however we can change the entire string with another string
name = name + " Shidlyali"
print(name) # now the entire string got changed