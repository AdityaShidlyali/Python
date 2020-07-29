# print negetive of number if the number is odd else print positive

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [i if (i%2 == 0) else -i for i in numbers]

print(new_list)