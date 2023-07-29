def countingSort(array):
    size = len(array)
    output = [0]*size

    count = [0]*10

    for j in range(size):
        count[array[j]] += 1
    
    for i in range(1, 10):
        count[i] += count[i-1]

    for i in range(size-1, -1, -1):
        output[count[array[i]]-1] = array[i]
        count[array[i]] -= 1
    
    for i in range(size):
        array[i] = output[i]
    