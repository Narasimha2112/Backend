# Reverse a list (Without Reverse)

nums = [1, 2, 3, 4, 5]
rev = []

#Loop Backward using Index
for i in range(len(nums)-1, -1, -1):
    rev.append(nums[i])
    
print(f"Reversed:", rev)

