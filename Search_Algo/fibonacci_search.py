def fibonacci_search(arr, target):
    n = len(arr)
    fibMMm2, fibMMm1 = 0, 1
    fibM = fibMMm2 + fibMMm1
    while fibM < n:
        fibMMm2, fibMMm1 = fibMMm1, fibM
        fibM = fibMMm2 + fibMMm1
    offset = -1
    while fibM > 1:
        i = min(offset + fibMMm2, n-1)
        if arr[i] < target:
            fibM, fibMMm1, fibMMm2 = fibMMm1, fibMMm2, fibM - fibMMm1
            offset = i
        elif arr[i] > target:
            fibM, fibMMm1, fibMMm2 = fibMMm2, fibMMm1 - fibMMm2, fibM - fibMMm1
        else:
            return i
    if fibMMm1 and offset < (n-1) and arr[offset+1] == target:
        return offset+1
    return -1
