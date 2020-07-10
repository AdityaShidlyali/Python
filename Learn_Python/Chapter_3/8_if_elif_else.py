"""
in python the if ... else if ... else by following syntax
if condition :
    statements
elif condition :
    statements
elif condition :
    statements
.
.
else :
    statements

This is used to check for multiple conditions
"""

age = input("Enter your age")
age = int(age)

if age == 0:
    print("You cant get the ticket")
elif 0 < age <=3 :
    print("The ticket price is : FREE")
elif 3 < age <= 10 :
    print("The ticket price is : Rs.50")
elif 10 < age <= 35 :
    print("The ticket price is : Rs.100")
else :
    print("The ticket price is : Rs.150")

