# Here is the Python implementation for the Coin Change Problem using
#  Dynamic Programming (Bottom-Up approach). This algorithm finds the
# minimum number of coins needed to make a specific target amount given
# a set of coin denominations

def coin_change(coins : list[int], amount:[int]) ->int:

    # Initialize dp array with infinity, size (amount + 1)
    # dp[i] will store the minimum coins needed to make amount 'i'
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1,amount+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i],dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else - 1


# examaple
if __name__ == "__main__":
    available_coin = [1,2,5]
    target_amount = 11

    result = coin_change(available_coin, target_amount)
    print(f"minimum coins needed for amount {target_amount} : {result}")