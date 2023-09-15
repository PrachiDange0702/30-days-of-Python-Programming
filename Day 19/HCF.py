def compute_hcf(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the HCF
hcf = compute_hcf(num1, num2)

# Print the result
print(f"The HCF of {num1} and {num2} is {hcf}")
