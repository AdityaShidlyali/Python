# list comprehension using if condition

numbers = list(range(1, 11))

# create the even numbers from 1 to 10 using list comprehension
even_numbers = [i for i in numbers if i%2 == 0]
print(even_numbers)
