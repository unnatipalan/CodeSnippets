#sortingwithlambda.py


cars = [('citroen', 'xsara', 1100), ('lincoln', 'navigator', 2000), ('bmw', 'x5', 1700)]

#sorting with the first element in the list
print(sorted(cars, key=lambda car: car[0]))


#sorting with the second element in the list
print(sorted(cars, key=lambda car: car[1]))


#sorting with the third element in the list
print(sorted(cars, key=lambda car: car[2]))
