def counting_sort(array):
    if not all(isinstance(x, int) for x in array):
        raise TypeError("Все элементы массива должны быть целыми числами для сортировки подсчётом.")

    size = len(array)
    output = [0] * size
    count = [0] * (max(array) + 1)

    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

    return array

def radix_sort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        counting_sort_for_radix(array, place)
        place *= 10
    return array

def counting_sort_for_radix(inputArray, placeValue):
    size = len(inputArray)
    outputArray = [0] * size
    countArray = [0] * 10

    for i in range(size):
        index = int(inputArray[i] / placeValue)
        countArray[index % 10] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i - 1]

    i = size - 1
    while i >= 0:
        index = int(inputArray[i] / placeValue)
        outputArray[countArray[index % 10] - 1] = inputArray[i]
        countArray[index % 10] -= 1
        i -= 1

    for i in range(size):
        inputArray[i] = outputArray[i]

def bucket_sort(array):
    bucket = []

    for i in range(len(array)):
        bucket.append([])

    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array
