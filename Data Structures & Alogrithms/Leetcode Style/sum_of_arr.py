# Problem 2: Sum of Array

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])                  # number of elements
    arr = list(map(int, data[1:]))    # array elements
    
    total = 0
    for num in arr:
        total += num 
        
    return total