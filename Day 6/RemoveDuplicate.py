def remove_duplicates(string):
    characters = list(string)
    unique_chars = []
    for char in characters:
        if char not in unique_chars:
            unique_chars.append(char)
    result = "".join(unique_chars)
    return result
input_string = input("Enter a string: ")
result_string = remove_duplicates(input_string)
print("String after removing duplicates:", result_string)
