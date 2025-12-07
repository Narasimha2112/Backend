def reverse_array(arr):
    """
    Reverse the list 'arr' in-place (modifies the original list).
    Also returns the same list for convenience.
    """
    left = 0                       # start pointer
    right = len(arr) - 1           # end pointer

    # Continue swapping until the two pointers meet or cross
    while left < right:
        # Swap elements at positions left and right
        arr[left], arr[right] = arr[right], arr[left]

        # Move left pointer to the right
        left += 1

        # Move right pointer to the left
        right -= 1

    return arr


# Example usage
nums = [1, 2, 3, 4, 5]
print(reverse_array(nums))  # Output: [5, 4, 3, 2, 1]
def reverse_array(arr):
    """
    Reverse the list 'arr' in-place (modifies the original list).
    Also returns the same list for convenience.
    """
    left = 0                       # start pointer
    right = len(arr) - 1           # end pointer

    # Continue swapping until the two pointers meet or cross
    while left < right:
        # Swap elements at positions left and right
        arr[left], arr[right] = arr[right], arr[left]

        # Move left pointer to the right
        left += 1

        # Move right pointer to the left
        right -= 1

    return arr


# Example usage
nums = [1, 2, 3, 4, 5]
print(reverse_array(nums))  # Output: [5, 4, 3, 2, 1]
