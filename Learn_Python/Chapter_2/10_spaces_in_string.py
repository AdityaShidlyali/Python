name = "      Aditya      "
dots = "............"

print(name + dots)

# lstrip() method removes the spaces which are on the left side of the string
print(name.lstrip() + dots)

# rstrip() method removes the spaces which are on the right side of the string
print(name.rstrip() + dots)

# strip() method removes the all the spaces irrespective of the position
print(name.strip() + dots)

# replace() method replaces the mentioned character with the expected character
# syntax : it has got two arguments to be passed 
# 1st one is character need to be relaced and second argument is the character which is need to be replaced
print(name.replace(" ", "") + dots)

# we can perform multiple methods on the strings (input the string and the character need to be counted with number of spaces)
name, char_to_cnt = input("Enter your name and character need to counted seperating them with comma : ").split(',')
print(f"Length of your name is {len(name)}")
"""
The following statement first removes the spaces from the name and then it makes
name to lowercase.

and then it removes all the spaces from the character need to be counted
and then it converts to lowercase() of the character which is need to be counted
"""
print(f"Count of character is {name.strip().lower().count(char_to_cnt.strip().lower())}")
