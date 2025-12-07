# Problem 1: Find Min & Max

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])                 # number of elements
    arr = list(map(int, data[1:]))   # read n integers
    
    # Initialize min and max
    current_min = arr[0]
    current_max = arr[0]
    
    # Traverse the array
    for num in arr[1:]:
        if num < current_min:
            current_min = num
        if num > current_max:
            current_max = num
    
    # Print in required format
    print(current_min, current_max)
