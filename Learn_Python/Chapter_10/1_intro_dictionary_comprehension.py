# to generate the following dictionary
# {1:1, 2:4, 3:9}

square = {num : num**2 for num in range(1, 5)}
print(square)

# to print the strings as well in the dictionary comprehension is :
square = {f"Square is {num} is {num**2}" for num in range(1, 5)}
print(square)

# word counter using dictionary comprehension :
name = "aditya"
word_count = {ch : name.count(ch) for ch in name}
print(word_count)