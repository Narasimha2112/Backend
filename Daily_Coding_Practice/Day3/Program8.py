#Reverse String Using loop

s = input("Enter a string: ")
rev = ""

for ch in s:
    rev = ch + rev  #Add characters in Reverse Order
    
print(f"Reversed : {rev}")

