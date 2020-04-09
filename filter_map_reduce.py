from functools import reduce  # reduce exists in the functools module.

aList = [1, 2, 3, 4]

filterList = list(filter(lambda n: n % 2 == 0, aList))  # returns a generator expression

mapList = list(map(lambda n: n * 2, filterList))  # returns a generator expression

addList = reduce(lambda a, b: a + b, mapList)  # returns a list

print(f'filtering only even numbers from {aList} into {filterList} using Filter function in Python')
print(f'Mapping to run a function on each value of {filterList} using map function in Python returns {mapList}')
print(f'Sum of values from {mapList} results into {addList} using Reduce function in Python')
