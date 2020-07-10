# by default the print function prints the data in new line
# by passing the "end" argument and mentioning the delimeter to it we can print the elements seperated by delimenter
# by passing the "sep" argument and mentioning the delimeter to it we can print (each) the elements seperating by delimeter
# please read both the above statements carefully to find the difference

print("09", "May", "2020", sep = "/")

n = input("Enter number of natural numbers required : ")
n = int(n)

i = 1
print("The required natural numbers are : ")
for i in range(1, n+1) :
    print(i, end = ' ') # inserts the space after the previous execution