def is_anagram(s, t):
    """
    Check if strings s and t are anagrams of each other.
    Returns True if they are anagrams, False otherwise.
    """
    # Quick length check: anagrams must have same length
    if len(s) != len(t):
        return False

    # Dictionary to count characters in s
    freq = {}

    # Count chars in s
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Subtract counts using chars from t
    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            # More of this char in t than in s
            return False

    # Optional: verify all zero (usually guaranteed now)
    # for val in freq.values():
    #     if val != 0:
    #         return False

    return True


# Example
print(is_anagram("listen", "silent"))  # True
print(is_anagram("rat", "car"))        # False
