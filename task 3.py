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


print(find_duplicates([1, 2, 3, 4, 2, 3, 4, 5, 6]))
