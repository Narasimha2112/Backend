#Sum of first n natural numbers

n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i
    
print(f"Sum of first {n} natural numbers are : {total}")
