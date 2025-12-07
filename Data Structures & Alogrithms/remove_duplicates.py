def remove_duplicates_sorted(nums):
    """
    Given a sorted list 'nums', remove duplicates in-place so that
    each element appears only once.
    Returns the list of unique elements (for understanding),
    but in interviews they often want the length (slow + 1).
    """
    if not nums:
        return []

    # slow is the index of the last unique element
    slow = 0

    # fast scans the array
    for fast in range(1, len(nums)):
        # When we find a new unique value
        if nums[fast] != nums[slow]:
            slow += 1                 # move slow forward
            nums[slow] = nums[fast]   # write the unique value at slow

    # Unique elements are now from index 0 to slow
    unique_part = nums[:slow + 1]
    return unique_part


# Example
nums = [1, 1, 2, 2, 2, 3, 4, 4]
print(remove_duplicates_sorted(nums))  # [1, 2, 3, 4]
