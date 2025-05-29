def kth(arr, k):
    if not arr:
        return None  # Handle empty array case
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    num_below = len(below)

    if k < num_below:
        return kth(below, k)
    elif k < num_below + len(equal):
        return pivot
    else:
        return kth(above, k - num_below - len(equal))