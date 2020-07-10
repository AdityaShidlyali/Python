def sub_list_count (list_1) :
    count = 0
    for i in list_1 :
        if type(i) == list :
            count += 1
    return count

my_list = [1, 2, 3, [4,3,2] , [34, 34, 1]]
print(sub_list_count(my_list))