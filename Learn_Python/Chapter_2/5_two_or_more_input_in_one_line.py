# we can also make the input as in the previous file that is 4_more_about_variables

# By default all the inputs will be in the form of string

# we give the delimeter .split() method to take the multiple input from the user. Example:
# here by default .split() method allows taking multiple inputs by seperating them with space
# here for .split() method the default delimeter is space
name, age = input("Enter your name and age seperating them with space : ").split()
print("Your name is : " + name)
print("Your age is : " + age)

# we can change the delimeter by invoking following statement
name, age = input("Enter your name and age seperating them with comma : ").split(',') # comma as delimeter
print("Your name is : " + name)
print("Your age is : " + age)

name, age = input("Enter your name and age seperating them with dot").split('.') # dot as delimeter
print("Your name is : " + name)
print("Your age is : " + age)