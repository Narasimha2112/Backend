def find_min_max(arr):
    """
    Find the minimum and maximum values in a non-empty list 'arr'.
    Returns a tuple: (min_value, max_value)
    """
    if not arr:
        # In interviews, they might specify arr is non-empty.
        # Here we handle empty list explicitly.
        raise ValueError("Array must not be empty")

    # Initialize both min and max with the first element
    current_min = arr[0]
    current_max = arr[0]

    # Start from index 1 because index 0 is already used
    for value in arr[1:]:
        # If current value is smaller than current_min, update current_min
        if value < current_min:
            current_min = value

        # If current value is larger than current_max, update current_max
        if value > current_max:
            current_max = value

    return current_min, current_max


# Example usage
nums = [3, 10, 6, 2, 8]
print(find_min_max(nums))  # Output: (2, 10)
