# Check if a string is Palindrome or not

s = input("Enter a string: ")

if s == s[::-1]:
    print(f"Palindrome")
else:
    print(f"Not a Palindrome")
    
    