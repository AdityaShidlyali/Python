# update method in python dictionaries

user_info = {
    'name' : "Aditya",
    'age' : 25,
    'fav_songs' : ["Kodaline", "Kronicle"],
    'fav_pc' : ['asus', 'acer', 'dell']
}

more_info = {
    'State' : 'Karnataka',
    'Origin' : 'India'
}

user_info.update(more_info)
print(user_info)

# the update method can also used to update the data of the perticular key and value pair in the existing dictionary
more_info = {'name' : 'aditya'}
user_info.update(more_info)
print(user_info)