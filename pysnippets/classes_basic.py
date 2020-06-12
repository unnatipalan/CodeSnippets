#creating a class
class User:
    pass

user1 = User() #an instance/object of the User class
user1.first_name = "Dave"
user1.last_name = "Bowman"
#do not capitalize field names 

print(f'first_name ssociated with class: {user1.first_name}')
print(f'last_name ssociated with class: {user1.last_name}')

#assigning values to the same variables
first_name = "Arthur"
last_name = "Clarke"

print(f'first_name and last_name not associated with a class: {first_name, last_name}')

#classes are used to make objects and each variable can have their own field values
user2 = User()

user2.favorite_book = '2001: A Space Odyssey'
user1.age = 38

#an object of the same class may not have the same fields
print(user1.age)
print(user2.favorite_book)


