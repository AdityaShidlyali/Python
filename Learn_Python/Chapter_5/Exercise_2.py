# using append() and pop() methods reverse the list
def reverse (list_1) :
    #return list_1[::-1] we can also do this to reverse the list
    rev_list = list()
    for i in range(len(list_1)) :
        popped_ele = list_1.pop()
        rev_list.append(popped_ele)
    return rev_list

my_list = ["Aditya", "Shidlyali"]
print(reverse(my_list))

print(my_list[::-1])