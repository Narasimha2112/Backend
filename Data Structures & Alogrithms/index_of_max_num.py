#Index of Maximum number in array
def index_of_max_num(arr):
    if not arr:
        return None
    
    max_value = arr[0]
    max_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
            
    return max_index