def make_change(n, coins):
    """
    Calculates the number of each coin needed to make change for amount n using a greedy approach.
    """
    change = {}
    for coin in coins:
        count = n // coin
        if count > 0:
            change[coin] = count
        n %= coin
    return change

# Coin values
coins = [500, 100, 10, 5, 1]

# Example usage
if __name__ == "__main__":
    # Test with a small amount for demonstration
    n = 10
    change = make_change(n, coins)
    print(f"For amount {n}:")
    for coin, count in change.items():
        print(f"{coin}: {count}")

    # User input
    try:
        amount = int(input("Enter the amount of money n: "))
        change = make_change(amount, coins)
        print(f"For amount {amount}:")
        for coin, count in change.items():
            print(f"{coin}: {count}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
