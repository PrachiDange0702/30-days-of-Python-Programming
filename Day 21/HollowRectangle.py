# Program to print a hollow rectangle of 5 rows and 6 columns
def hollow_rectangle(rows, columns):
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
      
hollow_rectangle(5, 6)
