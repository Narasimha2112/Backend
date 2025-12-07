def rotate_array(nums, k):
    """
    Rotate the list 'nums' to the right by 'k' steps in-place.
    Uses the reverse method.
    """
    n = len(nums)
    if n == 0:
        return nums

    # Normalize k to avoid extra full rotations
    k = k % n

    # Helper function to reverse a portion of the array in-place
    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # Step 1: Reverse entire array
    reverse(0, n - 1)
    # Step 2: Reverse first k elements
    reverse(0, k - 1)
    # Step 3: Reverse remaining n-k elements
    reverse(k, n - 1)

    return nums


# Example
nums = [1, 2, 3, 4, 5, 6, 7]
print(rotate_array(nums, 3))  # [5, 6, 7, 1, 2, 3, 4]
