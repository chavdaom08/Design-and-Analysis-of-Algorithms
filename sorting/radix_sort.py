def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of digits at current place value (exp)
    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

    # Update count[i] so it contains actual positions in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (iterate backwards to maintain stable sorting)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # Copy sorted elements back into original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if not arr:
        return arr

    # Find the maximum number to know number of digits
    max_val = max(arr)

    # Do counting sort for every digit (exp is 1, 10, 100, ...)
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


# Example usage:
numbers = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_numbers = radix_sort(numbers)
print("Sorted array:", sorted_numbers)


# Time Complexity: O(d * (n + b))
# Space Complexity: O(n + b)