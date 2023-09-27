def generate_spiral_matrix(n):
    # Initialize the matrix with zeros
    matrix = [[0] * n for _ in range(n)]

    # Define the initial values
    num = 1
    left, right, top, bottom = 0, n - 1, 0, n - 1

    while num <= n * n:
        # Traverse right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Traverse down
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Traverse left
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Traverse up
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix

def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f"{num:2d}", end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the size of the spiral matrix: "))
    spiral_matrix = generate_spiral_matrix(n)
    print("Spiral Matrix:")
    print_matrix(spiral_matrix)
