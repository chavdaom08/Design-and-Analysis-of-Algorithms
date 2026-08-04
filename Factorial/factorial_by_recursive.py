def factorial(n):
    if n == 0 or n == 1:   
        return 1
    # base case 

    return n * factorial(n-1)
    #  recursive case 

# Example
num = 3
print(f"the factorial{num} is :{factorial (num)} ")