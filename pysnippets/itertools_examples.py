from itertools import *

# Easy joining of two lists into a list of tuples
for i in zip([1, 2, 3], ['a', 'b', 'c']):
    print(i)
    
    
# The count() function returns an interator that 
# produces consecutive integers, forever. izip doesn't seem to work with it anymore

for i in zip(count(1), ['Bob', 'Emily', 'Joe']):
    print(i)

#Dropwhile function
# Function to be passed
# as an argument
def is_positive(n):
    return n > 0 
  
value_list =[5, 6, -8, -4, 2]
result = list(dropwhile(is_positive, value_list)) 
   
print(result)


#GroupBy
#Example1 
  
L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
  
# Key function
key_func = lambda x: x[0] #Sorting the list L. Check sortingwithlambda.py for more info 
  
for key, group in groupby(L, key_func):
    print(key + " :", list(group))
    
#Example2

a_list = [("Animal", "cat"), 
          ("Animal", "dog"), 
          ("Bird", "peacock"), 
          ("Bird", "pigeon")]
  
  
an_iterator = groupby(a_list, lambda x : x[0])
  
for key, group in an_iterator:
    key_and_group = {key : list(group)}
    print(key_and_group)
