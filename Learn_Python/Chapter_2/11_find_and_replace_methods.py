string = "she is beautiful and she is good dancer"

"""
The find method got 3 arguments some_string.find(sub_string_to_start_with, number_where_the_search_need_to_be_started)
"""
is_pos_1 = string.find("is")
is_pos_2 = string.find("is", is_pos_1 + 1) # the search starts from "s beatiful and ....."

print("First is position : ", is_pos_1)
print("Second is position : ", is_pos_2)

"""
The replace method has got three arguments some_string.replace(sub_string_need_to_replace, sting_need_to_replace_with, number_how_many_to_be_replaced)
"""
print(string.replace("is", "was", 1)) # replaces only first "is" with "was"
print(string.replace("is", "was", 2)) # replaces two number os "is" with "was"