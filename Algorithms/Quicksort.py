data = [56,89,41,2,7,0,6,894,5,7,856,89,45,15,75,10]
# print(data)

"""
Steps:
1. Pick the all items
2. Make as smaller chucks to compare(max 2 items in each chunk)
3. Compare and swap items in each chunk
4. swap the chunks accordingly
"""


def quick_sort(arr, start=None, end=None):
    if start is None:
        start = 0

    if end is None:
        end = len(arr)-1

    if start >= end:
        return

    p = qs_partation(arr, start, end)
    quick_sort(arr, start, p-1)
    quick_sort(arr, p+1, end)


def qs_partation(arr, start, end):
    pivot = arr[start]
    l = start + 1
    h = end

    while True:
        while l <= h and arr[h] >= pivot:
            h = h - 1
        while l <= h and arr[l] <= pivot:
            l = l + 1

        if l <= h:
            arr[l], arr[h] = arr[h], arr[l]
        else:
            break

    arr[start], arr[h] = arr[h], arr[start]

    return h


print(data)
quick_sort(data)
print(data)
