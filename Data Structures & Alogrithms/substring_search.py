def strstr(haystack, needle):
    """
    Return the index of the first occurrence of 'needle' in 'haystack'.
    If 'needle' is not found, return -1.
    Behaves similar to haystack.find(needle).
    """

    # Edge case: empty needle usually returns 0
    if needle == "":
        return 0

    n = len(haystack)
    m = len(needle)

    # We only need to check positions where needle can fully fit
    # from 0 to n - m
    for i in range(n - m + 1):
        # Compare substring haystack[i:i+m] with needle
        if haystack[i:i + m] == needle:
            return i

    # If not found
    return -1


# Example
print(strstr("hello world", "world"))  # 6
print(strstr("aaaaa", "bba"))          # -1
print(strstr("abc", ""))               # 0
