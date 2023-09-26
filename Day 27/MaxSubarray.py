def max_subarray_sum(arr):
    max_sum = arr[0]  # Initialize max_sum with the first element of the array
    current_sum = arr[0]  # Initialize current_sum with the first element of the array

    for num in arr[1:]:
        # Update current_sum to be the maximum of the current element and the current sum plus the current element
        current_sum = max(num, current_sum + num)
        
        # Update max_sum to be the maximum of max_sum and current_sum
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr)
print("Maximum subarray sum:", result)
