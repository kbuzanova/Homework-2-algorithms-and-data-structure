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
    pass


# Testing function for students
def test_merge_k_sorted_arrays():
    test_cases = [
        # Example Case
        ([
            [1, 3, 5],
            [2, 4, 6],
            [0, 7, 8]
        ], [0, 1, 2, 3, 4, 5, 6, 7, 8]),

        # Single array
        ([[1, 2, 3]], [1, 2, 3]),

        # Empty arrays
        ([
            [],
            [1, 2, 3],
            []
        ], [1, 2, 3]),

        # All arrays empty
        ([
            [],
            [],
            []
        ], []),

        # Arrays of different sizes
        ([
            [1, 5, 10],
            [2, 4],
            [3],
            [0, 6, 7, 8]
        ], [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]),

        # Arrays with negative numbers
        ([
            [-5, -3, 0],
            [-10, -1],
            [-7, -4]
        ], [-10, -7, -5, -4, -3, -1, 0]),

        # Large arrays with overlapping elements
        ([
            [1, 1, 2, 2],
            [2, 3, 3, 4],
            [0, 5, 5, 6]
        ], [0, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6]),

        # Very large K with small arrays
        ([[i] for i in range(100)], list(range(100))),

        # Large array sizes
        ([
            list(range(0, 100, 10)),
            list(range(5, 105, 10)),
            list(range(2, 102, 10))
        ], sorted(list(range(0, 100, 10)) + list(range(5, 105, 10)) + list(range(2, 102, 10)))),
    ]

    for idx, (arrays, expected) in enumerate(test_cases, start=1):
        result = merge_k_sorted_arrays(arrays)
        print(f"Test Case {idx}:")
        print(f"Input: arrays={arrays}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}\n")
        assert result == expected, f"Test case {idx} failed"

test_merge_k_sorted_arrays()
