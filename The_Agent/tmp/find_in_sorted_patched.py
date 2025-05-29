def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start > end: #Fix: The base case was incorrect. It should be start > end, not start == end.
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid - 1) #Fix: The end index should be mid -1 for the left subarray.
        elif x > arr[mid]:
            return binsearch(mid + 1, end) #Fix: The start index should be mid + 1 for the right subarray.
        else:
            return mid

    return binsearch(0, len(arr) - 1) #Fix: The end index should be len(arr) -1.