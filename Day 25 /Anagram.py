# Python program to check two strings are anagram or not
def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the lengths of the two strings are the same
    if len(str1) != len(str2):
        return False

    # Create dictionaries to store character frequencies
    char_count1 = {}
    char_count2 = {}

    # Count characters in the first string
    for char in str1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    # Count characters in the second string
    for char in str2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    # Compare the dictionaries
    return char_count1 == char_count2

str1 = "listen"
str2 = "silent"
if are_anagrams(str1, str2):
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams.")
