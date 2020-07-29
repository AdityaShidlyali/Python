# set comprehension is used rarely

# to print the sqares of the number form 1 to 10 :
s = {i**2 for i in range(1, 11)}
print(s)

# to print the first character of the list of strings :
name = ["aditya", "shidlyali", "mahesh"]
s = {i[0] for i in name}
print(s)