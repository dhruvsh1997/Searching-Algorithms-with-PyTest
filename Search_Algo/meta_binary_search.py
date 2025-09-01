def meta_binary_search(arr, target):
    n = len(arr)
    step = 1 << (n.bit_length() - 1)  # largest power of 2 <= n
    idx = -1
    while step > 0:
        if idx + step < n and arr[idx + step] <= target:
            idx += step
        step >>= 1
    return idx if arr[idx] == target else -1
