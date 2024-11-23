def top_k_frequent_elements(arr, k):
    frequency = [0] * 1001
    for num in arr:
        frequency[num] += 1
    frequency_pairs = [
        [num, frequency[num]] for num in range(1, 1001) if frequency[num] > 0
    ]
    frequency_pairs.sort(key=lambda x: x[1], reverse=True)
    return [frequency_pairs[i][0] for i in range(k)]


data = [1, 1, 1, 2, 2, 3, 6, 7]
k = 4
print(top_k_frequent_elements(data, k))
