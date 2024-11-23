import random


def random_array(size, lower_bound=-1000, upper_bound=1000):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]


def quick_sort_abs(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if abs(x) < abs(pivot)]
    middle = [x for x in arr[:-1] if abs(x) == abs(pivot)] + [pivot]
    right = [x for x in arr[:-1] if abs(x) > abs(pivot)]

    return quick_sort_abs(left) + middle + quick_sort_abs(right)

pass


def basic_test(sorting_func):
    arr = [5, 4, 3, 2, 1]
    arr = sorting_func(arr)
    res = sorted(arr, key=abs)
    assert arr == res, f"Expected {res}, but my sort got {arr}"
    print("\033[92mBasic test passed\033[0m")


def random_test(sorting_func):
    arr = random_array(5)
    print("Random array: ", arr)
    arr = sorting_func(arr)
    print("Sorted array: ", arr)
    res = sorted(arr, key=abs)
    assert arr == res, f"Expected {res}, but my sort got {arr}"
    print("\033[92mRandom test passed\033[0m")


def medium_test(sorting_func):
    arr = random_array(500)
    arr = sorting_func(arr)
    res = sorted(arr, key=abs)
    assert arr == res, f"Expected {res}, but my sort got {arr}"
    print("\033[92mMedium test passed\033[0m")


def big_test(sorting_func):
    arr = random_array(10000)
    arr_copy = arr.copy()

    import time
    start = time.time()
    arr = sorting_func(arr)
    end = time.time()
    print(f"Time to sort 10,000 elements: {end - start:.6f} seconds")

    start = time.time()
    arr_copy.sort(key=abs)
    end = time.time()
    print(f"Time to sort 10,000 elements with built-in sort: {end - start:.6f} seconds")

    assert arr == arr_copy, f"Expected {arr_copy}, but my sort got {arr}"
    print("\033[92mBig test passed\033[0m")


if __name__ == "__main__":
    sorting_func = quick_sort_abs
    basic_test(sorting_func)
    random_test(sorting_func)
    medium_test(sorting_func)
    big_test(sorting_func)