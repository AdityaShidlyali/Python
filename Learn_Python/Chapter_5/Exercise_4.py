# do the following operation
# [1,2,3,4,5,6,7,8,9,10] ---> print : [[2,4,6,8], [1,3,5,7,9]]

def assign_list (list_1) :
    odd_list, even_list = list(), list()
    for i in list_1 :
        if i%2 == 0 :
            even_list.append(i)
        else :
            odd_list.append(i)
    # output_list = [even_list, odd_list] we can also return the output list
    return [even_list,odd_list]

my_list = [1,2,3,4,5,6,7,8,9,10]
print(assign_list(my_list))