# dictionary comprehension using if else

# to create the dictionary like following :
# {1 : odd, 2 : even, 3 : odd}

d = {i : ("even" if i%2 == 0 else 'odd') for i in range(1, 10)}
print(d)