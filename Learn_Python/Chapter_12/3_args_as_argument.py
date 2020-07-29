def tot_all (*args):
    total = 0
    for i in args:
        total += i
    print(total)


num = [1, 2, 3]
# tot_all(num) this will be considered as single list not as elements of the args.
tot_all(*nums) # this will be unpacked using the * operator.
# * operator is applicable for all the linear data structures except dictionary.