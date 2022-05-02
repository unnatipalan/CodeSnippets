#Map() is a built-in Python function used to apply a function to a sequence of elements like a list or dictionary

def square_it_func(a):
    return a * a

x = map(square_it_func, [1, 4, 7])
print(x) # prints '[1, 16, 49]'

def multiplier_func(a, b):
    return a * b

x = map(multiplier_func, [1, 4, 7], [2, 5, 8])
print(x) # prints '[2, 20, 56]'
