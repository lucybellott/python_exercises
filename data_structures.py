# Sequence Types
    
# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

# Reading Information From Lists
#2. ✅ Return the first pet name
print(pet_names[0])


#3. ✅ Return all pet names beginning from the 3rd index
print(pet_names[3:])


#4. ✅ Return all pet names before the 3rd index
print(pet_names[:3])


#5. ✅ Return all pet names beginning from the 3rd index and up to the 7th
print(pet_names[3:7])


#6. ✅ Find the index of a given element => .index()
print(pet_names.index('Rose'))


#7. ✅ Reverse the original list => .reverse()

# pet_names.reverse()
# print(pet_names)


#8. ✅ Return the frequency of a given element => .count()

print(pet_names.count('Rose'))


# Updating Lists
#9. ✅ Change the first name to all uppercase letters => .upper()

print(pet_names[0].upper())


#10. ✅ Append a new name to the list => .append()

pet_names.append('Whicket')
print(pet_names)

#11. ✅ Add a new name at a specific index => .insert()

pet_names.insert(0, 'Porkchops')
print(pet_names)

#12. ✅ Add two lists together => +

print([1,2,3] + [4,5,6])


#13. ✅ Remove the final element from the list => .pop()

print(pet_names.pop())


#14. ✅ Remove element by specific index => .pop()
print(pet_names.pop(2))

#15. ✅ Remove a specific element => .remove()

pet_names.remove("Lea")
print(pet_names)

#16. ✅ Remove all pet names from the list => .clear()

#Tuple
# 📚 Review:
    # Mutable, Immutable <=> Changeable, Unchangeable

#17. ✅ Create a Tuple of 10 pet ages => () 

pet_ages = (2,3,3,5,6,7,8,9,10,11)


#18. ✅ Print the first pet age => []

print(pet_ages[0])

# Testing Mutability 
#19. ✅ Attempt to remove an element with ".pop" (should error)


#20. ✅ Attempt to change the first element (should error) => []


# Tuple Methods
#21. ✅ Return the frequency of a given element => .count()

print(pet_ages.count(3))

#22. ✅ Return the index of a given element  => .index()
print(pet_ages.index(5))

#23. ✅ Create a Range 
# Note:  Ranges are primarily used in loops

print(range(10))

# Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods
pet_fav_food = {'house plants', 'fish', 'bacon'}

# Dictionaries (SAME FORMAT AS JSON)
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'Rose', 'age':11, 'breed':'domestic long'}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
pet_info_spot = dict(name='Spot', age=25, breed='boxer')

# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
# print(pet_info_rose['temperament'])
print(pet_info_rose['name'])


#28. ✅ Print the pet attribute of "age" using ".get"

    # Note: ".get" is preferred over bracket notation in most cases 
    # because it will return "None" instead of an error


# Updating 
#29. ✅ Update Rose's age to 12 => []

pet_info_rose['age'] = 12
print(pet_info_rose['age'])

#30. ✅ Update Spot's age to 26 => .update({...})
pet_info_spot.update({'age': '26'})
print(pet_info_spot['age'])



# Deleting
#31. ✅ Delete Rose's age using the "del" keyword => []

del pet_info_rose['age']
print(pet_info_rose)


#32. ✅ Delete Spot's age using ".pop"

pet_info_spot.pop('age')
print(pet_info_spot)


#33. ✅ Delete the last item for Rose using "popitem()"

pet_info_rose.popitem()
print(pet_info_rose)

# Loops 
pet_info = [
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

#34. ✅ Loop through a range of 10 and print every number within the range

for num in range(10):
    print(num)


#35. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number

for num in range(50, 60, 2):
    print(num)


#36. ✅ Loop through the "pet_info" list and print every dictionary 
for pet in pet_info:
    print(pet)

#37. ✅ Create a function that takes a list a parameter 
    # The function should use a "for" loop to loop through the list and print each item 
    # Invoke the function and pass it "pet_names" as an argument

    def pet_stuff(list):
        for pet in list:
            print(pet)

    pet_stuff(pet_names)         


#38. ✅ Create a function that takes a list as a parameter
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 

    def counter_test(list):
        counter = 0
        while counter < len(list):
            counter += 1

        return counter

    print(counter_test(pet_names))   




#39. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dictionaries", "name" and "age" as parameters 
        # Create an index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param 
            # and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dictionary containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'Pet not found'
    
    # def pet_finder(list, name, age):
    #     index = 0
    #     while (index < len(list) -1 and list[index]['name'] != name):
    #             index += 1
                
    #             if list[index]['name'] == name:
    #                 list[index]['age'] = age

    #                 return list
    #             else:
    #               return 'Pet not found'

    #     print(pet_finder(pet_info, 'Spot', 50))      


    def update_pet_age(list, name, age):
    
        index = 0
    
        while(list[index]['name'] != name and index < len(list) - 1):
            index += 1

        if (list[index]['name'] == name):
            list[index]['age'] = age
            return list
        
        else:
            return 'Pet Not Found!'

#Pet Does Exist / Age is Updated
print(update_pet_age(pet_info, 'Spot', 50))



# map like 
#40. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase


# find like
#41. ✅ Use list comprehension to find a pet named spot


# filter like
#42. ✅ Use list comprehension to find all of the pets under 3 years old
