# range method has got the three arguments
# range(start_argument, stop_argument-1, step_argument)
# which returns the range of data between start and stop argument

n = input("Enter how many even numbers are required : ")
n = int(n)
r = range(0, n+n, 2)

for i in r :
    print(i)