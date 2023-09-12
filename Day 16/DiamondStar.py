# Diamond star pattern program
def print_diamond_pattern(n):
    # Upper part of the diamond
    for i in range(1, n + 1, 2):
        spaces = (n - i) // 2
        stars = i
        print(" " * spaces + "*" * stars)

    # Lower part of the diamond
    for i in range(n - 2, 0, -2):
        spaces = (n - i) // 2
        stars = i
        print(" " * spaces + "*" * stars)

# Input the number of rows (you can change this number)
num_rows = int(input("Enter the number of rows for the diamond pattern: "))

if num_rows % 2 == 0:
    print("Please enter an odd number for a symmetric diamond.")
else:
    print_diamond_pattern(num_rows)
