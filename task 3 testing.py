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

def find_duplicates(arr):
    arr = merge_sort(arr)
    result = []
    i = 0
    n = len(arr)
    while i < n:
        count = 1
        while i + 1 < n and arr[i] == arr[i + 1]:
            count += 1
            i += 1
        if count > 1:
            result.append((arr[i], count))
        i += 1
    return result



assert find_duplicates([1, 2, 3, 4, 2, 3, 4, 5, 6]) == [(2, 2), (3, 2), (4, 2)], "Test case 1 failed"
assert find_duplicates([1, 2, 3, 4, 5]) == [], "Test case 2 failed"
assert find_duplicates([1, 1, 1, 1, 1]) == [(1, 5)], "Test case 3 failed"
assert find_duplicates([1, 2, 3, 3, 3, 4, 4, 5, 19, 5, 20]) == [(3, 3), (4, 2), (5, 2)], "Test case 4 failed"
assert find_duplicates([1, 7, 2, 3, 4, 5, 6, 7, 8, 9, 10, 7]) == [(7, 3)], "Test case 5 failed"



def big_test():
    arr = random_array(10000)
    unique_arr = list(set(arr))
    sample = random.sample(unique_arr, 10)
    arr = sample + unique_arr + sample
    duplicates = find_duplicates(arr)
    expected_duplicates = [(i, 3) for i in sorted(sample)]
    print(f"Found duplicates: {duplicates}")
    print(f"Expected duplicates: {expected_duplicates}")
    assert duplicates == expected_duplicates, "Big test failed"
big_test()



