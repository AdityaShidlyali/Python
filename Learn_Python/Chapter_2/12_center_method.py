name = input("Enter your name : ")

# center() method makes the string center and it starts adding the mentioned character from the left side of the string
# syntax : some_string.center(number_greater_than_length_of_string, character_need_to_insert)

# this start putting the stars from the left side of the string
print(name.center(len(name) + 3, "*")) # see the difference between this line and the next line
print(name.center(len(name) + 4, "*"))