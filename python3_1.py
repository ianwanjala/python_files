#outputto print anything use print()

print ("Hello World")

#statemnts need not terminate with semi-colons
#print is a function; #it takes an argument 
# that is displayed on screen

#data types in pythong
x=5 # int data types
y=2.5 # float data type
my_string = ("hello there") # str data type
is_true= True # boolean data type
is_false =False #boolean data type 
my_first_list = [1,2,3] #list data structure
non_type = None  #NonType data type

print (type(x))
print (type(y))
print (type(my_string))
print (type(is_true))
print (type(is_false))
print (type(my_first_list))
print (type(non_type))
print (type(my_first_list))

#Tuple data structure
fieldsets =('Book Details', {'fields':('book','imprint','id')}), ('Availability',{'fields':('status','due_back')})

print (type (fieldsets))
print (fieldsets)

#handling input in python
# Input function allows use to input data and store it in a variable

print("Please enter your first name")

first_name = input ("First Name:")

print ("Please enter your last name")
last_name = input ("Last Name:")

#Basic input manipulation in python

first_name = 'john'
last_name = 'mark'

print (first_name+""+last_name)

#we can also use formatted string to format output
#formated strings in python

print(f"{first_name} {last_name}")

#capitalize the first letter
print (last_name.capitalize())

#change entire string to uppercase
print (last_name.upper())

#change entire string to lowercase
print (last_name.casefold())

note = "The quick brown fox jumped over the lazy dog"
print (note)
print (note.count("dog"))

#conditional statements in python
print ("please enter your age")
age = int(input("Age:"))

if age <= 21: # if evaluates a given condition
    print ("Eligible to drive PSV")# execute if true
    
else: # evaluates if second condition is false
        print("Not eligible to drive") #execute if true

#Conditional statements in Python
#A small application to compute grade based on marks input evaluation

print ("Please enter your mark")
mark = int(input("Mark: "))

if mark >=70:
    print ("Passed. Grade A")
elif mark >=60:
    print ("Passed. Grade B")
elif mark>=50:
    print ("Passed. Grade C")
else:
    print ("Fail. Grade D")


# loops in python;, we use 'for..in' to create loops in python
#create a list with items
item_list = [2, "Mary", 4, "Mark", 6,8,10]

#item represents an instance of the list
#therefore, we are going through all the items and displaying them

for item in item_list:
    print (item)

#loops in python
first_name ="joseph"

#loops also privide access to the string elements

for char in first_name:
    print (char)

#for ... range allows looping through a more specific and user-defined range

for i in range (0,101,5):
    print (i)

#while loop in python

count = 0
while (count <=10):
    print (f"Counter is currently at {count}")
    if (count%2 ==0):
        print (f"{count} is even")
        break
    else:
        print (f"{count} is odd")
        #count +=1
        #break
        print ("Loop complete")
        

# 4 main data structure in python; list, tupple, set, dictionary (dict)
#Lists -A sequence of values that can be modified. Lists can accept value of different types
#Characteristics
#List items are ordered, changeable, and allow duplicate values
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#creating  a populated list.
#Syntax:  list_name=[item1,item2, item3,item4]
fruits=["Orange","Peach","Mango","Plum"]
#Printing first element of the list
print(fruits[0])
#priniting last element of the list
print(fruits[-1])

#creating  a populated list.
#Syntax: list_name = [item1, item2, item3,item4]
fruits=["Orange","Peach","Mango","Plum"]

#looping through entire list and printing the elements
for i in fruits:
    print(i)
#sorting list in alphabetical order
fruits.sort()
#displaying the sorted list
print(fruits)


#Creating and initializing a set
my_cities = {"Kampala", "Kigali", "Nairobi", "Mombasa", "Arusha", "Nairobi"}
#printing all the set elements
print(my_cities)
#printing the length of the set
print(len(my_cities))
#printing the type of structure
print(type(my_cities))

#add items to set
my_cities.add("Cape Town")
print(my_cities)
other_cities = {"Nakuru", "Naivasha", "Mwanza","Jiji", "Busia"}
my_cities.update(other_cities)
print(my_cities)

