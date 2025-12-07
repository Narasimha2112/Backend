# Problem 4: Check if Array is Sorted

def solve():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    is_sorted = True
    
    #compare each pair arr[i],arr[i+1]
    for i in range(n-1):
        if arr[i] > arr[i + 1]:
            is_sorted = False
            break
        
    print("YES" if is_sorted else "NO")