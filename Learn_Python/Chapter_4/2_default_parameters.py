# if by default the arguments are assigned to some value then they become the default variable for that perticular function

def full_name ( first_name, last_name = "unknown", age = None) :
    print(f"First name : {first_name} \nLast name : {last_name} \nAge : {age}")

full_name("Aditya")

# if we pass the value to the function arguments then only their values will changed otherwise the values of the variables remain default
full_name("Aditya" , "Shidlyali", 20)