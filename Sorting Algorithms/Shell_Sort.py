def shellSort(array):
    i = len(array) // 2

    while i > 0:
        for j in range(i, len(array)):
            temp = array[j]
            k = j
            while k >= i and array[k-i] > temp:
                array[k] = array[k-i]
                k -= i
            array[k] = temp
        i //= 2
