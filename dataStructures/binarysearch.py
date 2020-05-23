#Recursion 

def binarySearch(A,key):
    low = 0
    high = len(A)-1

    while low <= high:
        
        mid = (low + high) // 2 

        if key == A[mid]:

            return True

        elif key < A[mid]:
            high = mid - 1
        
        else:
            low = mid + 1
    
    return False

array = sorted([1,10,23,13,3,41])

print("Does the element exists in the array?", binarySearch(array,45))