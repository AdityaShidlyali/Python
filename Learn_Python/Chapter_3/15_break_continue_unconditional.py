for i in range (1, 11) :
    if i == 5 :
        break # the loop stops when the condition becomes true
    print(i, end = ' ')

print('\n')
for i in range (1, 11) :
    if i == 5 :
        continue # this skips the statements following it so it skips printing the number 5
    print(i, end = ' ')
