# do the following operation with the list
# ['abc', 'tuv', 'xyz'] ---> ['cba', 'vut', 'zyx']

def reverse (list_1) :
    rev_list = list()
    for i in list_1 :
        rev_list.append(i[::-1])
    return rev_list

my_list = ['abc', 'tuv', 'xyz']
print(reverse(my_list))