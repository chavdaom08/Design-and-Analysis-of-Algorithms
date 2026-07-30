def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Example 
number = 5
print(f"The factorial of {number} is: {factorial(number)}")


# Time Complexity:O(n)
# Space Complexity:O(1)