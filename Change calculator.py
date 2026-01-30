def print_coin_ways(n, coins, index=0, current=[]):
    """
    Recursively prints all possible ways to make change for amount n using the given coins.
    """
    if n == 0:
        print(current)
        return
    if index >= len(coins):
        return
    coin = coins[index]
    max_count = n // coin
    for count in range(max_count + 1):
        new_current = current + [coin] * count
        print_coin_ways(n - count * coin, coins, index + 1, new_current)

# Coin values
coins = [500, 100, 10, 5, 1]

# Example usage
if __name__ == "__main__":
    # Test with a small amount for demonstration
    n = 10
    print(f"All possible ways to make {n} using coins {coins}:")
    print_coin_ways(n, coins)

    # User input
    try:
        amount = int(input("Enter the amount of money n: "))
        print(f"All possible ways to make {amount} using coins {coins}:")
        print_coin_ways(amount, coins)
    except ValueError:
        print("Invalid input. Please enter an integer.")
