# *args with the normal parameters

def tot_all(num, *args) : # the first '2' from the formal parameter will not be considered as the args it will be considered as the num
    total = 0
    for i in args :
        total += i
    print(total)


tot_all(2, 2, 2, 2)    