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

def merge_k_sorted_arrays(arrays):
    if not arrays:
        return []
    merged_array = arrays[0]
    for i in range(1, len(arrays)):
        merged_array = merge(merged_array, arrays[i])
    return merged_array


k = 3
arrays = [[1, 3, 5], [2, 4, 6], [0, 7, 8]]

result = merge_k_sorted_arrays(arrays)
print(result)