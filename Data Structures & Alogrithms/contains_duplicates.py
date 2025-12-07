#Contains Duplicates
def containsDuplicates(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False