
c = ['New York', 'Seoul', 'Beijing']
p = ['USA', 'Korea', 'China']

# create a dictionary by joining lists
cp = {}
for x, y in enumerate(c):
    cp[y] = p[x]
    print(cp)

addict = [
    ['john', 'smith'],
    ['jane', 'Smith']
    ]

# interesting implementation of list comprehension to generate a dictionary of list values and their string length
newflat = [{innerlist: len(innerlist)}
           for sublist in addict
           for innerlist in sublist
           if len(innerlist) < 5 ]

print(newflat)