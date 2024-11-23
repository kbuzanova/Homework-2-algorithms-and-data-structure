def quick_sort_abs(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if abs(x) < abs(pivot)]
    middle = [x for x in arr[:-1] if abs(x) == abs(pivot)] + [pivot]
    right = [x for x in arr[:-1] if abs(x) > abs(pivot)]

    return quick_sort_abs(left) + middle + quick_sort_abs(right)
