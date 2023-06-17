def sliding_window_maximum(nums, k):
    n = len(nums)
    max_values = []

    for i in range(n - k + 1):
        window = nums[i:i+k]
        max_value = max(window)
        max_values.append(max_value)

    return max_values

# Example usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
max_values = sliding_window_maximum(nums, k)
print("Input array:", nums)
print("Sliding window size:", k)
print("Sliding window maximums:", max_values)
