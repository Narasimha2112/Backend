# Count vowels in a string

s = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0

for ch in s:
    if ch in vowels:
        count += 1
        
print("Number of Vowels: ",count)