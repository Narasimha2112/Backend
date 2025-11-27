# Count Vowels in a string using loop

text = input("Enter a string: ").lower()
count = 0
vowels = "aeiou"

for ch in text:
    if ch in vowels:
        count += 1
print(f"Vowels count : {count}")