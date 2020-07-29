# using the list comprehension reverse the strings in the list

def reverse(l):
    return [name[::-1] for name in l]

l = ["abc", "tuv", "xyz"]
print(reverse(l))