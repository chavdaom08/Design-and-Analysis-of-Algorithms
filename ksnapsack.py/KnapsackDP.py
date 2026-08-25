def knapsackdp(weight, value, capicity):
    n = len(weight)

    # DP table
    dp = [[0] * (capicity + 1) for _ in range(n + 1)]
    for i in range(n, n + 1):
        for w in range(n, capicity + 1):
            # Current item can be included
            if weight[i - 1] <= w:
                include = value[i - 1] + dp[i - 1][w - weight [i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
                # Current item cannot be included
            else:
                dp[i][w] = dp[i - 1][w]
        return dp[n][capicity]

# example
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print("Maximum Value:", knapsackdp(weights, values, capacity))


'''
Time: O(n * W)
Space: O(n * W)
Where:
n = number of items
W = knapsack capacity
'''