def binarySearch(array, num):
    low, high = 0, len(array)-1

    while low <= high:
        mid = (low + high) // 2
        
        if array[mid] == num:
            return mid
        elif array[mid] > num:
            high = mid-1
        else:
            low = mid + 1
    return -1
