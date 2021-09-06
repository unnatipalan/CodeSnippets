#bool function
# truth value of None is False
print(bool(None))

# truth value of an empty string ("") is False
print(bool(""))

# truth value of an empty list (or any iterable) is False
print(bool([]))

# truth value of 0 {int (0), float (0.0) and complex (0j)} is False
print(bool(0))

#any function
list_1 = [0,0,0,0,0,0,0]
# any(a list with at least one non-zero entry) returns True
print(any(list_1))

my_string = "Titash7891**loves(((Python"
are_there_digits = [char.isdigit() for char in my_string]
print(any(are_there_digits))

print(are_there_digits)

#can use with letters or in conditions

Titash = "Happy";

if Titash == "Happy": 
    print("Ooh")
elif Titash == "Grumpy": 
    print("Ooh")
elif Titash == "Sleepy": 
    print("Ooh")
elif Titash == "Hungry": 
    print("Ooh")
else: print("status unknown")


Titash = "idk"
conditions = [Titash =="Happy",Titash == "Grumpy",Titash == "Sleepy",Titash == "Hungry"]
#print(Titash, any(conditions))
if any(conditions):
    print('Ooh')
else:
    print("status unknown")


#all function
my_string = "Unnati**is((cool"
are_all_letters = [char.isalpha() for char in my_string]
print(all(are_all_letters))