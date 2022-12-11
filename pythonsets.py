#sets in python
super_cities={"New York", "Washington", "Carlifonia", "Oakland", "LA"}
print(super_cities)


#declaring and initializing a tuple
car_tuple = ("Toyota", "BMW", 25, "Merc")
#printing the elements in the tuple
print (car_tuple)
#retrieving the first element of a tuple
print(car_tuple[0])

#Fetch the length of the tuple
print (len(car_tuple))
#car_tuple [1] = "Mazda"
print(car_tuple)
print(type(car_tuple))
#convert tuple to list
car_list = list(car_tuple)

#check the type of structure
print(type(car_list))
#Modify the list
car_list[1] = "Mazda"
new_car_tuple = tuple(car_list)
#check the new tuple composition
print(new_car_tuple)
print(car_tuple)

# Declaring a dictionary
my_phone = {
    "Brand" : "Samsung",
    "Make" : "Galaxy",
    "Version" : "S21",
    "YoM" : 2021,
    "Origin" : "South Korea"
}

# Print the entire dictionary
print(my_phone)
# Access a value by its key
print(f'My phone make is: {my_phone["Make"]} and the version is : {my_phone["Version"]}')


# A nested dictionary
my_phone = {
    "phone_one": {
        "Brand": "Samsung",
        "Make": "Galaxy",
        "Version": "S21",
        "YoM": 2021,
        "Orign": "South Korea"
        }, 
    "phone_two": {
        "Brand": "Apple",
        "Make": "iPhone",
        "Version": "13",
        "YoM": 2021,
        "Orign": "USA"
        }
}

print(my_phone["phone_one"])
print(my_phone["phone_two"])
for phone in my_phone:
    print(my_phone[phone])

