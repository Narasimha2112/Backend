class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        # Check every possible pair (i, j)
        for i in range(n):
            for j in range(i + 1, n):
                # If the pair adds up to the target, return their indices
                if nums[i] + nums[j] == target:
                    return [i, j]
