def sum_of_array(arr):
    """
    Return the sum of all numbers in arr.
    """
    total = 0  # start with 0, neutral element for addition

    # Go through each element and add it to total
    for value in arr:
        total += value  # same as total = total + value

    return total


# Example usage
nums = [1, 2, 3, 4]
print(sum_of_array(nums))  # Output: 10

