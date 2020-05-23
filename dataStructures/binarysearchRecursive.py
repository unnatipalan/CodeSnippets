def binarySearch(array,key,low,high):
    if low > high :
        return False
    else :
        mid = (low + high) // 2
        if key == array[mid]:
            return True
        
        elif key < array[mid] :
            return binarySearch(array,key,low,mid-1)
        
        else:
            return binarySearch(array,key,mid+1,high)

A = [1,4,5,6,7,9,99,123,145]

print("Is the element in the list? ",binarySearch(array=A,key=99,low=0,high=len(A)-1))