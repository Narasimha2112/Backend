#Using Hashing
class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store number -> index
        seen = {}

        # Loop through the list once
        for i, num in enumerate(nums):
            # Find the complement needed to reach the target
            complement = target - num

            # If complement is already in the dictionary,
            # we have our answer
            if complement in seen:
                # seen[complement] is the index of the complement
                # i is the current index
                return [seen[complement], i]

            # Otherwise, store the current number and its index
            seen[num] = i
