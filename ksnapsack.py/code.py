def knapsack(weights, values, capacity):
    #  Initialize a 1D list with zeros
    dp = [0] * (capacity + 1)

    for i in range(len(values)):
        weight = weights[i]
        value = values[i]


        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], value + dp[w - weight])
            

    return dp[capacity]


# Example 
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_val = knapsack(weights, values, capacity)
print("Max value in knapsack =", max_val)