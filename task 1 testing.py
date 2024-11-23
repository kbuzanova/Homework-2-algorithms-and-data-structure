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

    pass


def check_sorted_tests():
    print("#1. Starting test cases for check_sorted")
    assert check_sorted([1, 2, 3, 4, 5]) == 1, "Test case 1 failed"
    assert check_sorted([5, 4, 3, 2, 1]) == -1, "Test case 2 failed"
    assert check_sorted([1, 2, 3, 5, 4]) == 0, "Test case 3 failed"
    assert check_sorted([1, 1, 1, 1, 1]) == 2, "Test case 4 failed"
    assert check_sorted([1, 2, 3, 3, 3, 4, 4, 5, 19, 5, 20]) == 0, "Test case 5 failed"
    print("\033[92mAll test cases passed\033[0m")


check_sorted_tests()
