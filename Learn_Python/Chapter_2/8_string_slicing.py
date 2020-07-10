# syntax string_variable[start_argument : stop_argument - 1 : step_argument]
# stop_argument stops at length-1

language = "Python Programming"

# it is not mandatory that we should mention the step_argument
print(language[:])
print(language[0:6])
print(language[-18:18])
print(language[10:18])

# we can skip some of the characters in the string and print by using step argument
print(language[::2]) # with the step of 2 means it prints the characters skipping with the step of 2

# we can print the reverse of the string using step argument
print(language[18::-1]) # we should mention the negative step_argument in the field of step_argument
# or
print(f"Reversed string is : {language[18::-1]}")

# we can reverse the string and assign it to the string variable
# here I assigned the len() method in the field of start argument to reverse and assign th reveresed string to variable
language = language[len(language)::-1]
print(language)