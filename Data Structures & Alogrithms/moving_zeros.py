def move_zeroes(nums):
    """
    Move all zeros in the list 'nums' to the end,
    while keeping the relative order of non-zero elements.
    The operation is done in-place.
    """
    # Position where the next non-zero should be placed
    pos = 0

    # First pass: move all non-zero values to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1

    # Second pass: fill the remaining positions with zeros
    while pos < len(nums):
        nums[pos] = 0
        pos += 1

    return nums  # returning for convenience


# Example
nums = [0, 1, 0, 3, 12]
print(move_zeroes(nums))  # [1, 3, 12, 0, 0]
