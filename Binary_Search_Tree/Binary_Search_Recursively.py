def binary_search_recursively(A, key, l, r):
    if l > r:
        return -1
    else:
        mid = (l+r)//2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binary_search_recursively(A,key, l, mid-1)
        elif key > A[mid]:
            return binary_search_recursively(A, key, mid+1, r)


A = [15, 21, 47, 84, 96]
found = binary_search_recursively(A, 21, 0, 4)
print('Result : ', found+1,'Position')