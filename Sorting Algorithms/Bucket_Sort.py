def bucketSort(array):
    bucket = []

    for i in range(len(array)):
        bucket.append([])

    for i in range(len(array)):
        index = int(array[i]*10)
        bucket[index].append(array[i])

    for b in bucket:
        b.sort()
    
    k = 0
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
