from .binary_search import binary_search

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    return binary_search(arr[min(i//2, n-1):min(i, n)], target) + (i//2 if i < n else n//2)
