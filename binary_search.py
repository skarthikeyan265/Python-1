# Binary Search in Python
nl = [1,2,3,4,5,6,7,8,9,10]
t = 3

def binary_search(nl, t):
    low, high = 0, len(nl)-1
    while low <= high:
        mid = (low + high ) // 2
        if nl[mid] == t:
            return mid
        elif nl[mid] < t:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search(nl, t))
