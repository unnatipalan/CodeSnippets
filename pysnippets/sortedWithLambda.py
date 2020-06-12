
# trying to sort a list with lambda function

alist = ['z', 'q', 'Hello', 'a']

sorted(alist,key=lambda w: w.lower()) # remember this returns a new sorted list

alist.sort(key=lambda w: w.lower()) # remember this changes the list items in place
print(alist)
