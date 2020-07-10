number_one = input ("Enter first number : ")
number_two = input ("Enter second number : ")

print("total is : ", number_one + number_two) # this dosent prints the total

# to convert them to integer we invoke int() method
number_one = int(number_one)
number_two = int(number_two)
total = number_one + number_two
print(total) # here total also becomes integer

# to convert them to float we invoke float() method
number_one = float(number_one)
number_two = float(number_two)
total = number_one + number_two # total also becomes float
print(total)