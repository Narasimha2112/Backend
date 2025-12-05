# Check if array is a palindrome

arr = [1, 2, 5, 1]

def Palindrome(arr):
    l, r = 0, len(arr)-1
    
    while l < r:
        if arr[l] != arr[r]:
            return "Not a Palindrome"
        l += 1
        r -= 1
    
    return "Palindrome"
    
    