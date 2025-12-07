#Index of Minimum number in array

def index_of_min_num(arr):
    if not arr:
        return None
    
    min_value = arr[0]
    min_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i
            
    return min_index