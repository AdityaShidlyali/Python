list_1 = ['orange', 'mango', 'banana', 'grapes']
list_2 = ['orange', 'mango', 'banana', 'grapes', [1, 2, 3, 4, 5], [100, 200, 300, 400, 500], list_1]

# accessing list inside the list
print(list_2[4][0], list_2[4][1], list_2[4][2])

print(list_2[6][1])