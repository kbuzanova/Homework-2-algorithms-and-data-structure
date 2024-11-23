def check_sorted(arr):
    non_descending_disorders = 0
    non_ascending_disorders = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            non_descending_disorders += 1
        if arr[i] > arr[i - 1]:
            non_ascending_disorders += 1

    if non_descending_disorders == 0 and non_ascending_disorders == 0:
        return 2
    elif non_descending_disorders == 0:
        return 1
    elif non_ascending_disorders == 0:
        return -1
    return 0
