# dictionaries are also the data structures in python

# what are dictionaries ?
# dictionaries are the unordered collectoin of data in "key : value" pair

# why we use dictionaries ?
# to overcome the limitations of the lists, because the lists cant represent the real data

# we create the dictionaries using brackets{}

dict_1 ={1 : "Aditya", 2 : "Shidlyali"} # first method of creating the dictionaries
print(type(dict_1)) # prints the type as dict
print(dict_1[1]) # prints Aditya

# dictionaries are mutable datastructures
dict_1 = dict(name = "Aditya", age = 25) # the dict must be invoked the keys here cannot be numbers
print(dict_1) # the name and the age here are in the form of string

# accessing the dictionaries values
# here the keys of the dictionaries acts as index numbers for accessing the data in the dictionaries
print(dict_1['name'])

# which type of the data can be stored in dictionaries
# we can store the tuples, lists, int, float, strings, dictionaries
user_info = {
    'name' : "Aditya",
    'age' : 25
}
print(user_info['name'])

# we can insert one dictionary to another dictionary also
user_info = {
    'user_1' : { # including more than one dictionaries in existing dictionaries is called data modeling
        'name' : "Aditya",
        'age' : 20,
        'fav_songs' : ["Kodaline", "Kronicle"],
        'fav_pc' : ['asus', 'acer', 'dell'] 
    },

    'user_2' : { # name of the dictionaries should be quoted
        'name' : "Aditya",
        'age' : 24,
        'fav_songs' : ["Kodaline", "Kronicle"],
        'fav_pc' : ['asus', 'acer', 'dell'] 
    }
} # NOTE : we should use the colon to assign the values to the keys
print(user_info)

# Adding data to empty dictionary
dict_1 = dict()
dict_1['name'] = "Aditya"
dict_1['age'] = 25
print(dict_1)