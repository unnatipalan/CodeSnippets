#filter to return values if True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Will return true if input number is even
def even(x):
    return x % 2 == 0
# non-pythonic approach
even_nums = []
for num in numbers:
    if even(num):
        even_nums.append(num)
 
print('Non-Pythonic Approach: ', even_nums)
# pythonic approach
even_n = filter(even, numbers)
print('Pythonic Approach: ', list(even_n))

# using lambda function
even_num = list(filter(lambda x: x%2 == 0, numbers))
print(f'Using lambda approach: {even_num}')

#zip to iterate over two lists
first = [1, 3, 8, 4, 9]
second = [2, 2, 7, 5, 8]
# Iterate over two or more list at the same time
for x, y in zip(first, second):
    print(x + y)