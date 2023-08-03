def linearSearch(array, num):
    for i,n in enumerate(array):
        if n == num:
            return i
    return -1
