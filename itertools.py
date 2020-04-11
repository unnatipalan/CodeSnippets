from itertools import *

# Easy joining of two lists into a list of tuples
for i in zip([1, 2, 3], ['a', 'b', 'c']):
    print(i)
# ('a', 1)
# ('b', 2)
# ('c', 3)

# The count() function re turns an interator that 
# produces consecutive integers, forever. This 
# one is great for adding indices next to your list 
# elements for readability and convenience
for i in zip(count(1), ['Bob', 'Emily', 'Joe']):
    print (i)
# (1, 'Bob')
# (2, 'Emily')
# (3, 'Joe')    

# The dropwhile() function returns an iterator that returns 
# all the elements of the input which come after a certain 
# condition becomes false for the first time. 
def check_for_drop(x):
    print('Checking: ', x)
    return (x > 5)

for i in dropwhile(check_for_drop, [2, 4, 6, 8, 10, 12]):
    print('Result: ', i)

# Checking: 2
# Checking: 4
# Result: 6
# Result: 8
# Result: 10
# Result: 12


