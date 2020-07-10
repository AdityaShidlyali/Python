# in keyword and itereators using dictionaries

user_info = {
    'name' : "Aditya",
    'age' : 25,
    'fav_songs' : ["Kodaline", "Kronicle"],
    'fav_pc' : ['asus', 'acer', 'dell']
}

# check if key exist in the dictionary or not
if 'name' in user_info.keys() :
    print("The key is present")
else :
    print("The keyword is not present")

# check whether the value is there or not
if 'Aditya' in user_info.values() :
    print("The value is present")
else :
    print("value is not present")

# looping in dictionary
for i in user_info :
    print(i) # this will only print only keys
for i in user_info.values() :
    print(i) # this will only print only values

# values() method
print(user_info.values()) # this will print all the values of the dictionaries
user_info_values = user_info.values()
print(user_info_values) # this will also print the values of the dictionary
print(type(user_info_values)) # this will print <class, dict_values> This will in the form of the list but it is not the list

# keys() method
print(user_info.keys()) # this will print all the keys of the dictionary
user_info_keys = user_info.keys()
print(user_info_keys) # this will print all the keys of the dictionary
print(type(user_info_keys)) # this will print <class, dict_keys> This will in the form of the list but it is not the list

# print all the values of the dictionary using values of the dictionary using for loop
for i in user_info :
    print(user_info[i])

# items() method
items = user_info.items()
print(items) # this will print all the values as well as keys in the form of tuples
print(type(items))

# printing keys and values to gether
for i,j in user_info.items() :
    print(f"The key {i} has the value {j}")

# using tuple unpacking in dictionary
for i in user_info.items() :
    print(i)