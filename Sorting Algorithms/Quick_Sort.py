def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi-1)
        quickSort(array, pi, high)

def partition(array, leftmost, rightmost):
    pivot = array[rightmost]
    i = leftmost -1

    for j in range(leftmost, rightmost):
        if array[j] <= pivot:
            i += 1
            array[j], array[i] = array[i], array[j]
        j += 1
    array[rightmost], array[i+1] = array[i+1], array[rightmost]

    return i + 1


data = [8, 7, 2, 1, 0, 9, 6]
quickSort(data, 0, len(data)-1)
print(data)