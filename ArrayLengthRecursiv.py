def list_length(lst):
    """
    Recursively calculates the length of the given list.
    """
    if not lst:
        return 0
    return 1 + list_length(lst[1:])

# Example usage
if __name__ == "__main__":
    # Test cases
    print("Length of []:", list_length([]))  # Output: 0
    print("Length of [1]:", list_length([1]))  # Output: 1
    print("Length of [1, 2, 3]:", list_length([1, 2, 3]))  # Output: 3
    print("Length of [1, 2, 3, 4, 5]:", list_length([1, 2, 3, 4, 5]))  # Output: 5
