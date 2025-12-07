def are_rotations(s1, s2):
    """
    Check if s2 is a rotation of s1.
    Example: s1 = 'abcd', s2 = 'cdab' -> True
    """
    # Lengths must be equal, else impossible
    if len(s1) != len(s2):
        return False

    # Concatenate s1 with itself
    doubled = s1 + s1

    # If s2 is a substring of doubled, it's a rotation
    return s2 in doubled


# Example
print(are_rotations("abcd", "cdab"))  # True
print(are_rotations("abcd", "acbd"))  # False
