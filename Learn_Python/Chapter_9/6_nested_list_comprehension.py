# to generate the list like below using nested list comprehension
numbers = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

nested_numbers = [[i for i in range(1, 4)] for i in range(1, 4)]
print(nested_numbers)