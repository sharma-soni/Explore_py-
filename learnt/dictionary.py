# dictionary
dict={"soni":24} #Element present in dictionary in the form of key and value pair
#Keys must be strings or hashable types
names_dict=[
    {"name":"soni","age":24},
    {"name":"priya","age":25},
    {"name":"prince","age":26},
] #List of dictionaries
# print(names_dict)
# If you want to access value of 1 you need index for that
# print(names_dict[1]) #start from 0 accessing 1st element
print(names_dict[1]["name"]) #accessing name of 1st element


# using for loop 
for name in names_dict:
    print(f"{name}:{names_dict[name]}")  #accessing name and age of each element in the list of dictionaries
# using for loop with index