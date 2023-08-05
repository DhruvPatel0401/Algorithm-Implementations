def binarySearch(array, lo, hi, num):
    if lo > hi:
        return -1
    mid = (lo+hi) // 2

    if array[mid] == num:
        return mid
    elif array[mid] > num:
        return binarySearch(array, lo, mid-1, num)
    else:
        return binarySearch(array, mid+1, hi, num)
