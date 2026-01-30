def find_paths(n, m, path="", row=0, col=0):
    """
    Recursively finds all paths from (0,0) to (n-1,m-1) moving only right or down.
    """
    if row == n - 1 and col == m - 1:
        print(path)
        return
    if row < n - 1:
        find_paths(n, m, path + "d", row + 1, col)
    if col < m - 1:
        find_paths(n, m, path + "r", row, col + 1)

# Example usage
if __name__ == "__main__":
    # Test with the example
    n = 2
    m = 3
    print(f"All paths for {n}x{m} maze:")
    find_paths(n, m)

    # User input
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        print(f"All paths for {rows}x{cols} maze:")
        find_paths(rows, cols)
    except ValueError:
        print("Invalid input. Please enter integers.")
