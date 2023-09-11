def fibonacci(n):
    fib_series = [0, 1]  # Initialize the first two Fibonacci numbers

    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]  # Calculate the next Fibonacci number
        fib_series.append(next_num)

    return fib_series

# Example usage:
n = 10  # Change n to the desired number of Fibonacci numbers
result = fibonacci(n)
print(result)
