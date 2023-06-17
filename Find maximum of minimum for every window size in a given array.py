def find_maximum_of_minimums(array):
    n = len(array)
    result = []

    for window_size in range(1, n+1):
        minimums = []
        for i in range(n - window_size + 1):
            window = array[i:i+window_size]
            minimums.append(min(window))
        
        result.append(max(minimums))

    return result

# Test case
arr = [10, 20, 30, 50, 10, 70, 30]
output = find_maximum_of_minimums(arr)
print(output)
