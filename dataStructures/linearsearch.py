def linearSearch(array,element):
    position = 0
    flag = False

    while position < len(array) and not flag: #Not flag allows us to exit the loop when we encounter our element
        if (array[position] == element):
            flag = True
        else:
            position = position + 1
    return flag

A = [10,15,16,89]

print("Is Element present in the Array: ",linearSearch(A,15))