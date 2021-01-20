def linear_search(A, key):
    index = 0
    while index < len(A):
        if A[index] == key :
            return index
        index = index + 1
    return -1



A = [84, 21, 47, 96, 15]
found = linear_search(A,96)
print('Result : ',found)
