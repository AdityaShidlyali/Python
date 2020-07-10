# add or delete the data in dictionary
user_info = {
    'name' : "Aditya",
    'age' : 25,
    'fav_songs' : ["Kodaline", "Kronicle"],
    'fav_pc' : ['asus', 'acer', 'dell']
}

# add data at the end of the dictionary
user_info['fav_movies'] = ['Dhoni', 'Steve Jobs']
print(user_info)

# pop method to delete the data in dictionary based on the key
# pop method also returns the deleted data from the dictionary
popped_item = user_info.pop('fav_movies')
print("The popped item is :", popped_item)

# popitem() method : it randomly removes the items in the dictionary
popped_item = user_info.popitem()
print(popped_item)