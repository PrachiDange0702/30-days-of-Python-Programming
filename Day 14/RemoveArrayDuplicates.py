def remove_duplicates(arr):
    # Convert the array to a set to remove duplicates
    unique_set = set(arr)
    
    # Convert the set back to a list
    unique_list = list(unique_set)
    
    return unique_list

# Example usage:
arr = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(arr)
print(result)  # Output: [1, 2, 3, 4, 5]
