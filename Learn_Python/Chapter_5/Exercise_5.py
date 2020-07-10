# do the following operation
# return the elements which are common in both the list [1,2,3,4] and [1,2,5,8,10]

def find_common (list_1, list_2) :
    output_list = list()
    for i in list_1 :
        if i in list_2 :
            output_list.append(i)
    return output_list

my_list_1 = [1,2,3,4]
my_list_2 = [1,2,5,8,10]

print(find_common(my_list_1, my_list_2))
