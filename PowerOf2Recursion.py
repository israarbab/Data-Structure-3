def recursive_multiply(a, b):
    """
    Recursively multiplies two numbers a and b.
    """
    if b == 0:
        return 0
    if b < 0:
        return -recursive_multiply(a, -b)
    return a + recursive_multiply(a, b - 1)

# Example usage
if __name__ == "__main__":
    # Test cases
    print("5 * 6 =", recursive_multiply(5, 6))  # 30
    print("3 * 4 =", recursive_multiply(3, 4))  # 12
    print("7 * 0 =", recursive_multiply(7, 0))  # 0
    print("2 * 10 =", recursive_multiply(2, 10))  # 20

    # User input
    try:
        a = int(input("Enter 'a' for a*b: "))
        b = int(input("Enter 'b' for a*b: "))
        result = recursive_multiply(a, b)
        print(f"1 iteration: {result}")
        print(f"N iteration: {result}")
    except ValueError:
        print("Invalid input. Please enter integers.")
