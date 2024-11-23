import random


def random_array(size, lower_bound=-1000, upper_bound=1000):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))

def merge(left_arr, right_arr):
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_arr) and right_pointer < len(right_arr):
        if left_arr[left_pointer] <= right_arr[right_pointer]:
            result.append(left_arr[left_pointer])
            left_pointer += 1
        else:
            result.append(right_arr[right_pointer])
            right_pointer += 1

    result.extend(left_arr[left_pointer:])
    result.extend(right_arr[right_pointer:])

    return result

    pass


def basic_test(sorting_func):
    arr = [5, 4, 3, 2, 1]
    sorted_arr = sorting_func(arr)
    assert sorted_arr == sorted(arr), f"Expected {sorted(arr)}, but my sort got {sorted_arr}"
    print("\033[92mBasic test passed\033[0m")


def random_test(sorting_func):
    arr = random_array(5)
    print("Random array: ", arr)
    sorted_arr = sorting_func(arr)
    print("Sorted array: ", sorted_arr)
    assert sorted_arr == sorted(arr), f"Expected {sorted(arr)}, but my sort got {sorted_arr}"
    print("\033[92mRandom test passed\033[0m")


def medium_test(sorting_func):
    arr = random_array(500)
    sorted_arr = sorting_func(arr)
    assert sorted_arr == sorted(arr), f"Expected {sorted(arr)}, but my sort got {sorted_arr}"
    print("\033[92mMedium test passed\033[0m")


def big_test(sorting_func):
    arr = random_array(10000)
    arr_copy = arr.copy()

    import time
    start = time.time()
    sorted_arr = sorting_func(arr)
    end = time.time()
    print(f"Time to sort 10,000 elements: {end - start:.6f} seconds")

    start = time.time()
    arr_copy.sort()
    end = time.time()
    print(f"Time to sort 10,000 elements with built-in sort: {end - start:.6f} seconds")

    assert sorted_arr == arr_copy, f"Expected {arr_copy}, but my sort got {sorted_arr}"
    print("\033[92mBig test passed\033[0m")


if __name__ == "__main__":
    sorting_func = merge_sort
    print("Merge sort")
    basic_test(sorting_func)
    random_test(sorting_func)
    medium_test(sorting_func)
    big_test(sorting_func)