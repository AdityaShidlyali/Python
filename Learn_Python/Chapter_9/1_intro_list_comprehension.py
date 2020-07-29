# list comprehension
# with the help of list comprehension we can create the list in one line

# for example a list of squares from 1 to 10
squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)

# using list comprehension :
squares2 = [i**2 for i in range(1, 11)]
print(squares2)

# create the list of negetive numbers from 1 to 10
neg = [-i for i in range(1, 11)]
print(neg)

# create the list of first character of the names of the list
names = ["Aditya", "Mahesh", "Suchitra"]
ch = [i[0] for i in names]
print(ch)