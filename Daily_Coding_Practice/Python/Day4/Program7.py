# Function using args
def multiply_all(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply_all(2, 3, 4))