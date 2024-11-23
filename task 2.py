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

print(merge_sort([5, 6, 8, 1, 2, 4]))

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = key


# Time complexity of merge sort is O(nlog(n)). Space complexity of merge sort is O(n) because
# there is a need for additional memory to combine sub-assemblies.
# Time complexity of insertion sort is O(n^2) in the worst case (O(n) in the best case).
# Space complexity of insertion sort is O(1) because it is sorting on the same place
# Stability
# Both of sorts is stable. Merge sort holds the relative order of identical elements,
# since it compares the elements in two subarrays and combines them in order of their appearance.
# Insertion sort also holds the order of identical elements, since when the element is inserted
# into the correct position, it only moves elements larger than the key.
# Performance on sorted or almost sorted arrays.
# Because of the fact that merge sort has same time complexity in every case (it goes through all array) it won't
# change on sorted or unsorted arrays.
# In the same time insertion sort very good performance on almost sorted or small arrays, since its time
# complexity is at best O(n) (when the array is already sorted). For nearly sorted arrays, the number of
# operations is minimal