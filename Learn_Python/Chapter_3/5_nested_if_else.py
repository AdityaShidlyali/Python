num = input("Enter a number between 1 and 20")
num = int(num)

num_win = 16

if num == num_win :
    print("You win")
else :
    if num > num_win :
        print("Too high")
        print("Try again")
    else :
        print("Too low")
        print("Try again")

# we can also include n if else statements in "if" or "else" blocks