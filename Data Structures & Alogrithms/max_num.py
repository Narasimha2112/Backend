# Maximum Number in Array
def max_in_array(arr):
    if not arr:
        return None  #or raise Error
    
    max_val = arr[0]
    for x in arr[1:]:
        if x > max_val:
            max_val = x
    return max_val

