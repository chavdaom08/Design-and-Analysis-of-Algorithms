p = [10, 30, 5, 60, 16]  
n = len(p) - 1
# Matrix dimensions: A1(10x30), A2(30x5), A3(5x60), A4(60x16)


dp = [[0] * n for _ in range(n)]

# L is the length of the matrix chain being evaluated
for L in range(2, n + 1):
    for i in range(n - L + 1):
        j = i + L - 1
        dp[i][j] = min(
            dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
            for k in range(i, j)
        )

print("Minimum multiplications:", dp[0][n - 1])


# Time Complexity: O(n^3)
# Space Complexity: O(n^2)