# print the squares of each numbers from 1 to 10

def find_sqares(list_1) :
    new_list = list()
    for i in list_1 :
        new_list.append(i**2)
    return new_list

my_list = list(range(1,11))
print(find_sqares(my_list))