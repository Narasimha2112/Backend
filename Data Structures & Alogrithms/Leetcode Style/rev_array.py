# Problem 3: Reverse Array

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])                  # number of elements
    arr = list(map(int, data[1:]))    # array elements

    left = 0 
    right = len(arr) - 1
    
    #Reverse using two Pointers
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        
    #print Reversed array
    return arr

