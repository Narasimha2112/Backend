def reverse_string(s):
    """
    Reverse the input string s and return the reversed string.
    Uses two-pointer technique.
    """
    # Strings are immutable, so convert to list of characters
    chars = list(s)
    left = 0
    right = len(chars) - 1

    # Swap characters from both ends
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    # Join list back into a string
    return "".join(chars)


# Example
print(reverse_string("hello"))   # "olleh"
print(reverse_string("abc"))     # "cba"
