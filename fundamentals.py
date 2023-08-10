pet_mood = "hungry"

#we can use set_trace to overwrite previously set values
#ipdb.set_trace()

if pet_mood == "hungry":
    print('Rose needs to be fed')
elif pet_mood == "rowdy":
    print('Rose needs a walk')
else:
    print('Rose is all set')        

# create ternary operations using pet_mood as a condition

#print('Rose neeeds to be fed') if pet_mood == "hungry" else print('Rose is all set')

#create function say_hello that returns "hello world!"

def say_hello(name):
    print(f"hello, {name}")

say_hello('Lucy')    

#can not invoke functions containing params without args  

def pet_status(pet_name, pet_mood):
    if pet_mood == "hungry":
        print(f"{pet_name} needs to eat")
    elif pet_mood == 'rowdy':
        print(f"{pet_name} needs a walk")
    else:
        print(f"{pet_name} is all set")        

pet_status('Snoopy', 'happy')
pet_status('Porkchops', 'hungry')