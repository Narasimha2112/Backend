""" 
Linear Search (O(n))

Search each element one by one.
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return "Invalid Target"
    
nums = [10, 20, 30, 40]
print(linear_search(nums, 50))