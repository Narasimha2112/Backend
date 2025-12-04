# Count vowels using function

def count_vowels(s):
    s = s.lower()
    vowels = "aeiou"
    count = 0
    
    for ch in s:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("Education"))