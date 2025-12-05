# Minimum Number in Array
def min_in_array(arr):
    if not arr:
        return None  #or raise Error
    
    min_val = arr[0]
    for x in arr[1:]:
        if x < min_val:
            min_val = x
    return min_val
