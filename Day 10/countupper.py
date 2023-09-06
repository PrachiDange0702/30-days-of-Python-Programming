# Count number of Uppercase characters in a file in python
def count_uppercase():
    count = 0
    file = open("hello.txt", "r")
    for line in file:
        for char in line:
            if char.isupper():
                count += 1
    file.close()
    print("Number of uppercase characters in the file: " + str(count))

count_uppercase()
