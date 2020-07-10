# word counter using dictionary
word_count = dict()

s = input("Enter string : ")
for char in s :
    word_count[char] = s.count(char)

print(word_count)