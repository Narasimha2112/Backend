def intersection_arrays(nums1, nums2):
    """
    Return the unique intersection of two lists.
    Each element in the result must be unique.
    """
    set1 = set(nums1)
    set2 = set(nums2)

    # Set intersection gives elements common to both sets
    result_set = set1 & set2

    # Convert back to list (order not guaranteed)
    return list(result_set)


# Example
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection_arrays(nums1, nums2))  # [2]
