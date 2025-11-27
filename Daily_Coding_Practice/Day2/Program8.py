#Count vowels in a string using list

text = "education"
vowels = ["a", "e", "i", "o", "u"]
count = 0

#Loop through Characters
for ch in text:
    if ch in vowels:
        count += 1

print("Vowel Count: ",count)
