# the in keyword searches for the required element in given data

name = input("Enter your name : ")
char = input("Enter the character in your name to check : ")

if char in name :
    print("The character is present")
else :
    print("The character is not present")
