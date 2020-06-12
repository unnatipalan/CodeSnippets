#unpacking values inside of tuples, lists and dictionaries

# from 13 cards
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' ]

#“*_” is used to specify the arbitrary number of arguments in the tuple.

# extract ace, 2, 3 only
ace, two, three, *_ = cards
print(f'Extracting ace :{ace}, two: {two}, three: {three}')

#In case we want to skip only one argument then we can replace “*_” by “_”
ace, _, three, *_ = cards
print(f'Extracting ace :{ace}, three: {three}')


#Python gives the syntax to pass optional arguments (*arguments) for tuple unpacking of arbitrary length.
#All values will be assigned to every variable in the order of their specification and all remaining values will be assigned to *arguments

# extract ace, [numbers], J, Q, K
dictionary = {'A':'ace', 2:'two', 3:'three'}

ace, *numbers = dictionary.keys()

print(ace, numbers)
