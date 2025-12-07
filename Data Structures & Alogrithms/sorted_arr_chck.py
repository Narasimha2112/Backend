def is_sorted(arr):
    """
    Check if the array 'arr' is sorted in non-decreasing order.
    Returns True if sorted, False otherwise.
    """
    # Loop until second last element, because we compare arr[i] with arr[i+1]
    for i in range(len(arr) - 1):
        # If current element is greater than next element,
        # array is not sorted in non-decreasing order.
        if arr[i] > arr[i + 1]:
            return False

    # If we never found arr[i] > arr[i+1], it's sorted
    return True


# Example usage
print(is_sorted([1, 2, 2, 3, 5]))  # True
print(is_sorted([1, 3, 2, 4]))     # False
