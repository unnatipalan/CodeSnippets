#Recursive

def binarySearch(array,key,low,high):
    if low > high :
        return False #item not found!
    else :
        mid = (low + high) // 2
        if key == array[mid]:
            return True
        
        elif key < array[mid] :
            return binarySearch(array=array,key=key,low=low,high=mid-1)
        
        else:
            return binarySearch(array=array,key=key,low=mid+1,high=high)

A = [1,4,5,6,7,9,99,123,145]

print("Is the element in the list? ",binarySearch(array=A,key=109,low=0,high=len(A)-1))